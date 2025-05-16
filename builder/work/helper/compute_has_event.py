from avefi_schema import model as efi

from adlib import people_provider, thesau_provider
from builder.base.utils import get_formatted_date, get_same_as_for_priref
from mappings.agent_type_enum import agent_type_enum
from mappings.cinematography_activity_type_enum import cinematography_activity_type_enum
from mappings.directing_activity_type_enum import directing_activity_type_enum
from mappings.editing_activity_type_enum import editing_activity_type_enum
from mappings.music_activity_type_enum import music_activity_type_enum
from mappings.producing_activity_type_enum import producing_activity_type_enum
from mappings.production_design_activity_type_enum import (
    production_design_activity_type_enum,
)
from mappings.writing_activity_type_enum import writing_activity_type_enum


def compute_has_event(self):
    # activity handling

    activities = []

    # cast

    cast_members = []

    xml_cast_list = self.xml.xpath("Cast")

    for xml_cast in xml_cast_list:
        try:
            name_list = xml_cast.xpath("cast.name/value/text()")
            priref_list = xml_cast.xpath("cast.name.lref/text()")
            _type = xml_cast.xpath("cast.credit_type/value[@lang='de-DE']/text()")

            # Currently only cast without type!
            if _type or not name_list or not priref_list:
                continue

            name = name_list[0]
            priref = priref_list[0]

            cast_members.append(
                efi.Agent(
                    type=_get_type_for_priref(
                        priref,
                        people_provider,
                    ),
                    has_name=name,
                    same_as=get_same_as_for_priref(
                        priref,
                        people_provider,
                        include_gnd=True,
                        include_filmportal=True,
                    ),
                )
            )
        except Exception as e:
            raise Exception("Problem with has_event (Cast):", e)

    if cast_members:
        activities.append(
            efi.CastActivity(
                type=efi.CastActivityTypeEnum.CastMember, has_agent=cast_members
            )
        )

    activity_to_type_mapping = [
        (efi.DirectingActivity, directing_activity_type_enum),
        (efi.CinematographyActivity, cinematography_activity_type_enum),
        (efi.EditingActivity, editing_activity_type_enum),
        (efi.WritingActivity, writing_activity_type_enum),
        (efi.ProductionDesignActivity, production_design_activity_type_enum),
        (efi.ProducingActivity, producing_activity_type_enum),
        (efi.MusicActivity, music_activity_type_enum),
    ]

    for activity, activity_type_enum in activity_to_type_mapping:
        for activity_type_name in activity_type_enum.keys():
            xml_entity_list = self.xml.xpath(
                f"Credits[credit.type/value[@lang='de-DE'][text()='{activity_type_name}']]"
            )

            for xml_entity in xml_entity_list:
                name_list = xml_entity.xpath("credit.name/value/text()")
                priref_list = xml_entity.xpath("credit.name.lref/text()")

                if not name_list or not priref_list:
                    continue

                name = name_list[0]
                priref = priref_list[0]

                activities.append(
                    activity(
                        type=activity_type_enum[activity_type_name],
                        has_agent=efi.Agent(
                            type=_get_type_for_priref(
                                priref,
                                people_provider,
                            ),
                            has_name=name,
                            same_as=get_same_as_for_priref(
                                priref,
                                people_provider,
                                include_gnd=True,
                                include_filmportal=True,
                            ),
                        ),
                    )
                )

    return efi.ProductionEvent(
        located_in=_get_located_in(self),
        has_date=_get_has_date(self),
        has_activity=activities,
    )


def _get_has_date(self):
    production_date_start = self.xml.xpath("Dating/dating.date.start/text()")
    production_date_start_prec = self.xml.xpath(
        "Dating/dating.date.start.prec/value[@lang='3'][text()='circa']/text()"
    )
    production_date_end = self.xml.xpath("Dating/dating.date.end/text()")
    production_date_end_prec = self.xml.xpath(
        "Dating/dating.date.end.prec/value[@lang='3'][text()='circa']/text()"
    )

    if production_date_start and production_date_end:
        return get_formatted_date(
            production_date_start[0],
            production_date_start_prec[0] if production_date_start_prec else None,
            production_date_end[0],
            production_date_end_prec[0] if production_date_end_prec else None,
        )


def _get_located_in(self):
    located_in = []

    xml_productions = self.xml.xpath("Production")

    try:
        for xml_production in xml_productions:
            production_country_list = xml_production.xpath(
                "production_country/value[@lang='de-DE']/text()"
            )
            priref_list = xml_production.xpath("production_country.lref/text()")

            if not production_country_list or not priref_list:
                continue

            production_country_name = production_country_list[0]
            priref = priref_list[0]

            located_in.append(
                efi.GeographicName(
                    has_name=production_country_name,
                    same_as=get_same_as_for_priref(
                        priref,
                        thesau_provider,
                        include_gnd=True,
                    ),
                )
            )
    except Exception as e:
        raise Exception("Problem with has_event.located_in:", e)

    return located_in


def _get_type_for_priref(priref, provider):
    try:
        xml_data = provider.get_by_priref(priref)
        record_type_list = xml_data.xpath("record_type/value[@lang='3']/text()")

        if not record_type_list:
            return efi.AgentTypeEnum.Person

        record_type = record_type_list[0]

        if record_type not in agent_type_enum:
            raise Exception("No mapping found for key:", record_type)

        return agent_type_enum[record_type]

    except Exception as e:
        raise Exception("Problem with has_agent.type computation:", e)
