from avefi_schema import model as efi
from adlib import thesau_provider, people_provider


def compute_has_subject(self):
    # Agent (Person) handling
    xml_content_persons = self.xml.xpath("Content_person")

    persons = []

    try:
        for xml_content_person in xml_content_persons:

            person_name_list = xml_content_person.xpath(
                "content.person.name/value/text()"
            )
            priref_list = xml_content_person.xpath("content.person.name.lref/text()")

            if not person_name_list or not priref_list:
                continue
            person_name = person_name_list[0]
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

                if "http://d-nb.info/gnd/" in source_number:
                    same_as.append(
                        efi.GNDResource(
                            id=source_number.split("/")[-1],
                        )
                    )

                if "https://www.filmportal.de/person/" in source_number:
                    same_as.append(
                        efi.FilmportalResource(
                            id=source_number.split("_")[-1],
                        )
                    )

                # does not occur in test data set
                if "http://vocab.getty.edu/page/tgn/" in source_number:
                    same_as.append(
                        efi.TGNResource(
                            id=source_number.split("/")[-1],
                        )
                    )

            # CURRENTLY WRONG !!!! HOW TO DECIDE WHICH AGENT TYPE ????

            person = efi.Agent(
                has_name=person_name,
                same_as=same_as,
                type=efi.AgentTypeEnum.Person,
            )
            persons.append(person)

    except Exception as e:
        raise Exception("Problem with Content_Subjects (Persons):", e)

    # Subject and GeographicName handling

    xml_content_subjects = self.xml.xpath("Content_subject")

    subjects = []
    geographic_names = []

    try:
        for xml_content_subject in xml_content_subjects:

            subject_name_list = xml_content_subject.xpath(
                "content.subject/value[@lang='de-DE']/text()"
            )
            priref_list = xml_content_subject.xpath("content.subject.lref/text()")

            if not subject_name_list or not priref_list:
                continue
            subject_name = subject_name_list[0]
            priref = priref_list[0]

            subject_xml = thesau_provider.get_by_priref(priref)
            sources_xml = subject_xml.xpath("Source")

            same_as = []

            for source_xml in sources_xml:
                source_number_list = source_xml.xpath("term.number/text()")
                if not source_number_list:
                    # sometimes a source is provided but the source_number field is just empty e.g. 8072.xml
                    continue
                source_number = source_number_list[0]

                if "http://d-nb.info/gnd/" in source_number:
                    same_as.append(
                        efi.GNDResource(
                            id=source_number.split("/")[-1],
                        )
                    )

                if "http://vocab.getty.edu/page/tgn/" in source_number:
                    same_as.append(
                        efi.TGNResource(
                            id=source_number.split("/")[-1],
                        )
                    )

                # does not occur in test data set
                if "https://www.filmportal.de/person/" in source_number:
                    same_as.append(
                        efi.FilmportalResource(
                            id=source_number.split("_")[-1],
                        )
                    )

            # decide if geographic oder subject
            term_types = subject_xml.xpath("term.type/value[@lang='3']/text()")

            if "Ort" in term_types:
                geographic_names.append(
                    efi.GeographicName(
                        has_name=subject_name,
                        same_as=same_as,
                    )
                )

            if "Ort" not in term_types:
                subjects.append(
                    efi.Subject(
                        has_name=subject_name,
                        same_as=same_as,
                    )
                )

    except Exception as e:
        raise Exception("Problem with Content_Subject (Subject, GeographicName):", e)

    return persons + subjects + geographic_names
