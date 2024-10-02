from adlib import thesau_provider, people_provider
from builder.adlib_to_avefi_mappings import (
    work_form_enum_mapping,
    work_variant_type_enum_mapping,
    title_type_enum_mapping,
)
from builder.base_builder import BaseBuilder
from avefi_schema import model as efi


class WorkBuilder(BaseBuilder):

    def build(self):
        primary_title, alternative_titles = self.title

        return efi.WorkVariant(
            has_form=self.has_form,
            has_genre=self.has_genre,
            has_subject=self.has_subject,
            is_part_of=self.is_part_of,
            same_as=self.same_as,
            type=self.type,
            described_by=super().described_by,
            has_event=self.has_event,
            has_alternative_title=alternative_titles,
            has_primary_title=primary_title,
            has_identifier=super().has_identifier,
        )

    @property
    def has_form(self):
        nfa_categories = self.xml.xpath("nfa_category/value[@lang='3']/text()")

        # Please check for correct logic
        if not nfa_categories:
            return None

        return [
            work_form_enum_mapping.get(nfa_category) for nfa_category in nfa_categories
        ]

    @property
    def has_genre(self):
        xml_content_genres = self.xml.xpath("Content_genre")

        genres = []

        try:
            for xml_content_genre in xml_content_genres:
                genre_name_list = xml_content_genre.xpath("content.genre/value/text()")
                priref_list = xml_content_genre.xpath("content.genre.lref/text()")
                if not genre_name_list or not priref_list:
                    # sometimes a genre is provided but the not name or priref e.g. 150007840.xml
                    continue
                genre_name = genre_name_list[0]
                priref = priref_list[0]
                # print(genre_name, priref)
                genre_xml = thesau_provider.get_by_priref(priref)
                sources_xml = genre_xml.xpath("Source")

                same_as = []

                for source_xml in sources_xml:
                    term_number_list = source_xml.xpath("term.number/text()")
                    if not term_number_list:
                        # sometimes a source is provided but the term_number field is just empty e.g. 8072.xml
                        continue
                    term_number = term_number_list[0]
                    if "gnd" in term_number:
                        same_as.append(
                            efi.GNDResource(
                                id=term_number.split("/")[-1],
                            )
                        )

                genre = efi.Genre(has_name=genre_name, same_as=same_as)
                genres.append(genre)

        except Exception as e:
            # when type not provided
            raise Exception("Problem with Content_Genre:", e)

        return genres

    @property
    def has_subject(self):
        xml_content_persons = self.xml.xpath("Content_person")

        persons = []
        try:
            for xml_content_person in xml_content_persons:

                person_name_list = xml_content_person.xpath(
                    "content.person.name/value/text()"
                )
                priref_list = xml_content_person.xpath(
                    "content.person.name.lref/text()"
                )

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
                    if "gnd" in source_number:
                        same_as.append(
                            efi.GNDResource(
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

        xml_content_subjects = self.xml.xpath("Content_subject")
        subjects = []

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
                    # Note how is it called source.number instead of term.number like in content_genre!
                    source_number_list = source_xml.xpath("term.number/text()")
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

                # decide if geographic oder subject
                term_types = subject_xml.xpath("term.type/value[@lang='3']/text()")

                if "Geograf. Schlagwort" in term_types:
                    subjects.append(
                        efi.GeographicName(
                            has_name=subject_name,
                            same_as=same_as,
                        )
                    )
                else:
                    subjects.append(
                        efi.Subject(
                            has_name=subject_name,
                            same_as=same_as,
                        )
                    )

        except Exception as e:
            raise Exception(
                "Problem with Content_Subject (Subject, GeographicName):", e
            )

        return persons + subjects

    @property
    def is_part_of(self):
        return super().belongs_to

    @property
    def same_as(self):
        # currently only generating "avefi:FilmportalResource"
        xml_alternative_numbers = self.xml.xpath("Alternative_number")

        try:
            for xml_alternative_number in xml_alternative_numbers:
                number_list = xml_alternative_number.xpath("alternative_number/text()")
                number_type_list = xml_alternative_number.xpath(
                    "alternative_number.type/value/text()"
                )
                if not number_type_list or not number_list:
                    # skip when not both are provided e.g. 150000691.xml
                    continue
                number_type = number_type_list[0]
                number = number_list[0]

                if number_type == "ref_filmportal":
                    return efi.FilmportalResource(id=number)
        except Exception as e:
            # when type not provided
            raise Exception("Problem with Alternative_number:", e)

        return None

    @property
    def type(self):
        worklevel_type = self.xml.xpath("worklevel_type/value[@lang='3']/text()")[0]

        return work_variant_type_enum_mapping.get(worklevel_type)

    @property
    def has_event(self):

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
                    efi.Agent(
                        type=efi.AgentTypeEnum.Person, has_name=name, same_as=same_as
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

        # directors

        xml_directors_list = self.xml.xpath(
            "credits[credit.type/value[text()='Regie']]"
        )

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
                    efi.Agent(
                        type=efi.AgentTypeEnum.Person, has_name=name, same_as=same_as
                    )
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

        production_date_start = self.xml.xpath(
            "Production_date/production.date.start/text()"
        )
        production_date_end = self.xml.xpath(
            "Production_date/production.date.end/text()"
        )

        has_date = None

        if production_date_start and production_date_end:
            has_date = (
                production_date_start[0]
                if production_date_start[0] == production_date_end[0]
                else f"{production_date_start[0]}/{production_date_end[0]}"
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
                    efi.GeographicName(
                        has_name=production_country_name, same_as=same_as
                    )
                )
        except Exception as e:
            raise Exception("Problem with has_event (location):", e)

        return efi.ProductionEvent(
            located_in=located_in, has_date=has_date, has_activity=activities
        )

    @property
    def title(self):

        xml_titles = self.xml.xpath("Title")
        titles = []

        for xml_title in xml_titles:
            title_text = xml_title.xpath("title/text()")
            title_type = xml_title.xpath("title.type/value[@lang='de-DE']/text()")
            title_article = xml_title.xpath("title.article/text()")

            full_title_text = title_text[0]
            ordering_title_text = None

            # if article present build combined title
            if title_article:  # Please check for correct logic
                full_title_text = title_article[0] + " " + title_text[0]
                ordering_title_text = title_text[0] + ", " + title_article[0]

            try:
                titles.append(
                    efi.Title(
                        has_name=full_title_text,
                        type=title_type_enum_mapping.get(title_type[0]),
                        has_ordering_name=ordering_title_text,
                    )
                )
            except IndexError:
                # When no title provided
                assert len(title_type) == 0
                titles.append(
                    efi.Title(
                        has_name=full_title_text,
                        type=efi.TitleTypeEnum.AlternativeTitle,
                        has_ordering_name=ordering_title_text,
                    )
                )
            except Exception as e:
                # when type not provided, should we omit?
                raise Exception("Problem with Title:", e)

        def title_sort(title):
            if str(title.type) == str(efi.TitleTypeEnum.PreferredTitle.text):
                return 0
            if str(title.type) == str(efi.TitleTypeEnum.SuppliedDevisedTitle.text):
                return 1
            return 2

        # Please check for correct logic
        titles.sort(key=lambda x: title_sort(x))

        return titles[0], titles[1:]
