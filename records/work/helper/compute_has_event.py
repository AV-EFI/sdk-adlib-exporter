from avefi_schema import model as efi

from axiell_collections import people_provider, thesau_provider
from mappings.loader import get_mapping
from records.base.base_record import XMLAccessor
from records.base.utils import (
    get_formatted_date,
    get_same_as_for_priref,
    get_mapped_enum_value,
)


def compute_has_event(xml: XMLAccessor):
    activities = []

    cast_members = []

    xml_cast_list = xml.get_all("Cast")

    for xml_cast in xml_cast_list:

        name = xml_cast.get_first("cast.name/value/text()")
        priref = xml_cast.get_first("cast.name.lref/text()")
        credit_type = xml_cast.get_first("cast.credit_type/value[@lang='de-DE']/text()")

        # Currently only cast without type!
        if credit_type is not None:
            continue

        if name is None or priref is None:
            continue

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

    if cast_members:
        activities.append(
            efi.CastActivity(
                type=efi.CastActivityTypeEnum.CastMember, has_agent=cast_members
            )
        )

    activity_to_type_mapping = [
        (efi.DirectingActivity, get_mapping("DirectingActivityTypeEnum")),
        (efi.CinematographyActivity, get_mapping("CinematographyActivityTypeEnum")),
        (efi.EditingActivity, get_mapping("EditingActivityTypeEnum")),
        (efi.WritingActivity, get_mapping("WritingActivityTypeEnum")),
        (efi.ProductionDesignActivity, get_mapping("ProductionDesignActivityTypeEnum")),
        (efi.ProducingActivity, get_mapping("ProducingActivityTypeEnum")),
        (efi.MusicActivity, get_mapping("MusicActivityTypeEnum")),
    ]

    for activity, activity_type_enum in activity_to_type_mapping:
        for activity_type_name in activity_type_enum.keys():
            xml_entity_list = xml.get_all(
                f"Credits[credit.type/value[@lang='de-DE'][text()='{activity_type_name}']]"
            )

            for xml_entity in xml_entity_list:
                name = xml_entity.get_first("credit.name/value/text()")
                priref = xml_entity.get_first("credit.name.lref/text()")

                if name is None or priref is None:
                    continue

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
        located_in=_get_located_in(xml),
        has_date=_get_has_date(xml),
        has_activity=activities,
    )


def _get_has_date(xml: XMLAccessor):
    production_date_start = xml.get_first("Dating/dating.date.start/text()")
    production_date_start_prec = xml.get_first(
        "Dating/dating.date.start.prec/value[@lang='3'][text()='circa']/text()"
    )
    production_date_end = xml.get_first("Dating/dating.date.end/text()")
    production_date_end_prec = xml.get_first(
        "Dating/dating.date.end.prec/value[@lang='3'][text()='circa']/text()"
    )

    if production_date_start is None or production_date_end is None:
        return None

    return get_formatted_date(
        production_date_start,
        production_date_start_prec,
        production_date_end,
        production_date_end_prec,
    )


def _get_located_in(xml: XMLAccessor):
    located_in = []

    xml_productions = xml.get_all("Production")

    for xml_production in xml_productions:
        production_country = xml_production.get_first(
            "production_country/value[@lang='de-DE']/text()"
        )
        priref = xml_production.get_first("production_country.lref/text()")

        if production_country is None or priref is None:
            continue

        located_in.append(
            efi.GeographicName(
                has_name=production_country,
                same_as=get_same_as_for_priref(
                    priref,
                    thesau_provider,
                    include_gnd=True,
                    include_tgn=True,
                ),
            )
        )

    return located_in


def _get_type_for_priref(priref, provider):
    xml = provider.get_by_priref(priref)
    record_type = XMLAccessor(xml).get_first("record_type/value[@lang='3']/text()")

    if record_type is None:
        return efi.AgentTypeEnum.Person

    agent_type = get_mapped_enum_value("AgentTypeEnum", record_type)

    if agent_type is None:
        return efi.AgentTypeEnum.Person

    return agent_type
