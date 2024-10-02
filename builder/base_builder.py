from avefi_schema import model as efi
import datetime
from abc import ABC, abstractmethod
from builder.adlib_to_avefi_mappings import (
    language_code_enum_mapping,
    language_usage_enum_mapping,
)


class BaseBuilder(ABC):
    def __init__(self, xml, allowed_parents):
        self.xml = xml
        self.allowed_parents = allowed_parents

    @abstractmethod
    def build(self):
        """Method to build the entity. Must be implemented by child classes."""

    @property
    def belongs_to(self):
        part_of_list = self.xml.xpath("Part_of/part_of.recordnumber/text()")
        if part_of_list:
            for priref in part_of_list:
                if priref not in self.allowed_parents:
                    raise Exception("Unresolvable reference")
        return [efi.LocalResource(id=priref) for priref in part_of_list]

    @property
    def has_identifier(self):
        priref = self.xml.xpath("priref/text()")[0]
        return efi.LocalResource(id=priref)

    @property
    def described_by(self):
        return efi.DescriptionResource(
            has_issuer_id="https://w3id.org/isil/DE-MUS-407010",
            has_issuer_name="Deutsche Kinemathek - Museum für Film und Fernsehen",
            last_modified=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        )

    @property
    def in_language(self):

        xml_languages_list = self.xml.xpath("Language")

        languages = []

        try:
            for xml_language in xml_languages_list:
                language_list = xml_language.xpath(
                    "language/value[@lang='de-DE']/text()"
                )
                language_type_list = xml_language.xpath(
                    "language.type/value[@lang='3']/text()"
                )
                if not language_list or not language_type_list:
                    # currently skipping if either one not provided
                    continue

                language = language_list[0]
                language_type = language_type_list[0]

                code = language_code_enum_mapping.get(language)
                usage = language_usage_enum_mapping.get(language_type)

                if code is True or usage is True:
                    # currently skipping if not mapped correctly
                    continue

                languages.append(
                    efi.Language(
                        code=code,
                        usage=usage,
                    )
                )

        except Exception as e:
            raise Exception("Problem with language:", e)

        return languages
