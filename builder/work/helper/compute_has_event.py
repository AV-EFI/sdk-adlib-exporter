from avefi_schema import model as efi
from adlib import people_provider, thesau_provider


def compute_has_event(self):
    # Currently only production event

    # activity handling

    activities = []

    # cast

    cast_members = []

    xml_cast_list = self.xml.xpath("cast")

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

            person_xml = people_provider.get_by_priref(priref)
            sources_xml = person_xml.xpath("Source")

            same_as = []

            for source_xml in sources_xml:
                # Note how is it called source.number in people.inf instead of term.number like in thesau.inf!
                source_number_list = source_xml.xpath("source.number/text()")
                if not source_number_list:
                    # sometimes a source is provided but the source_number field is just empty e.g. 8072.xml
                    continue
                source_number = source_number_list[0]
                if "gnd" in source_number:
                    same_as.append(
                        efi.GNDResource(
                            id=source_number.split("/")[-1],
                        )
                    )
            cast_members.append(
                efi.Agent(type=efi.AgentTypeEnum.Person, has_name=name, same_as=same_as)
            )
        except Exception as e:
            raise Exception("Problem with has_event (Cast):", e)

    if cast_members:
        activities.append(
            efi.CastActivity(
                type=efi.CastActivityTypeEnum.CastMember, has_agent=cast_members
            )
        )

    # directors

    xml_directors_list = self.xml.xpath("credits[credit.type/value[text()='Regie']]")

    directors = []
    for xml_director in xml_directors_list:
        try:
            name_list = xml_director.xpath("credit.name/value/text()")
            priref_list = xml_director.xpath("credit.name.lref/text()")

            if not name_list or not priref_list:
                # priref and name not listed for example: see 150010458.xml
                continue

            name = name_list[0]
            priref = priref_list[0]

            person_xml = people_provider.get_by_priref(priref)
            sources_xml = person_xml.xpath("Source")
            # print(person_name, priref)

            same_as = []

            for source_xml in sources_xml:
                # Note how is it called source.number in people.inf instead of term.number like in thesau.inf!
                source_number_list = source_xml.xpath("source.number/text()")
                if not source_number_list:
                    # sometimes a source is provided but the source_number field is just empty e.g. 8072.xml
                    continue
                source_number = source_number_list[0]
                if "gnd" in source_number:
                    same_as.append(
                        efi.GNDResource(
                            id=source_number.split("/")[-1],
                        )
                    )
            directors.append(
                efi.Agent(type=efi.AgentTypeEnum.Person, has_name=name, same_as=same_as)
            )

        except Exception as e:
            raise Exception("Problem with has_event (Regie, Director):", e)

    if directors:
        activities.append(
            efi.DirectingActivity(
                type=efi.DirectingActivityTypeEnum.Director, has_agent=directors
            )
        )

    # date handling

    production_date_start = self.xml.xpath("Dating/dating.date.start/text()")
    production_date_start_prec = self.xml.xpath(
        "Dating/dating.date.start.prec/value[@lang='3'][text()='circa']/text()"
    )
    production_date_end = self.xml.xpath("Dating/dating.date.end/text()")
    production_date_end_prec = self.xml.xpath(
        "Dating/dating.date.end.prec/value[@lang='3'][text()='circa']/text()"
    )

    has_date = None

    if production_date_start and production_date_end:
        production_date_start_value = production_date_start[0] + (
            "~" if production_date_start_prec else ""
        )
        production_date_end_value = production_date_end[0] + (
            "~" if production_date_end_prec else ""
        )
        has_date = (
            production_date_start_value
            if production_date_start_value == production_date_end_value
            else f"{production_date_start_value}/{production_date_end_value}"
        )

    # location handling

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

            production_country_xml = thesau_provider.get_by_priref(priref)
            sources_xml = production_country_xml.xpath("Source")

            same_as = []

            for source_xml in sources_xml:
                # Note how is it called source.number instead of term.number like in content_genre!
                source_list = source_xml.xpath("source/text()")
                source_number_list = source_xml.xpath("term.number/text()")
                if not source_list or not source_number_list:
                    continue
                source = source_list[0]
                source_number = source_number_list[0]
                if source == "DNB":
                    same_as.append(
                        efi.GNDResource(
                            id=source_number.split("/")[-1],
                        )
                    )

            located_in.append(
                efi.GeographicName(has_name=production_country_name, same_as=same_as)
            )
    except Exception as e:
        raise Exception("Problem with has_event (location):", e)

    return efi.ProductionEvent(
        located_in=located_in, has_date=has_date, has_activity=activities
    )
