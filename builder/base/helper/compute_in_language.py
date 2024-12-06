from avefi_schema import model as efi
from mappings import language_usage_enum_mapping, language_code_enum_mapping


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
