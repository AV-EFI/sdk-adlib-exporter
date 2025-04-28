from avefi_schema import model as efi

from mappings.language_code_enum_mapping import language_code_enum_mapping
from mappings.language_usage_enum_mapping import language_usage_enum_mapping


def compute_in_language(self):

    xml_languages_list = self.xml.xpath("Language")

    languages = []

    try:
        for xml_language in xml_languages_list:
            language_list = xml_language.xpath("language/value[@lang='de-DE']/text()")
            language_type_list = xml_language.xpath(
                "language.type/value[@lang='3']/text()"
            )
            if not language_list or not language_type_list:
                continue

            language = language_list[0]
            language_type = language_type_list[0]

            if language not in language_code_enum_mapping:
                raise Exception("No mapping found for key:", language)

            if language_type not in language_usage_enum_mapping:
                raise Exception("No mapping found for key:", language_type)

            if (
                language_code_enum_mapping[language] is None
                or language_usage_enum_mapping[language_type] is None
            ):
                continue

            languages.append(
                efi.Language(
                    code=language_code_enum_mapping[language],
                    usage=language_usage_enum_mapping[language_type],
                )
            )

    except Exception as e:
        raise Exception("Problem with language:", e)

    return languages
