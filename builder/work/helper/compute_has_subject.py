from avefi_schema import model as efi

from adlib import thesau_provider, people_provider
from builder.base.utils import get_same_as_for_priref


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

            # CURRENTLY WRONG !!!! HOW TO DECIDE WHICH AGENT TYPE ????

            person = efi.Agent(
                has_name=person_name,
                same_as=get_same_as_for_priref(
                    priref,
                    people_provider,
                    include_gnd=True,
                    include_filmportal=True,
                    include_tgn=True,
                ),
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

            same_as = get_same_as_for_priref(
                priref,
                thesau_provider,
                include_gnd=True,
                include_filmportal=True,
                include_tgn=True,
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
