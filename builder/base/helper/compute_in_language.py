from avefi_schema import model as efi

from builder.base.base_builder import BaseBuilder, XMLContainer
from builder.base.utils import get_mapped_enum_value
from mappings.language_code_enum_mapping import language_code_enum_mapping
from mappings.language_usage_enum_mapping import language_usage_enum_mapping


def compute_in_language(record: BaseBuilder):

    xml_languages_list = record.xml.get_all("Language")

    languages = []

    for xml_language in xml_languages_list:

        language = XMLContainer(xml_language).get_first(
            "language/value[@lang='de-DE']/text()"
        )
        language_type = XMLContainer(xml_language).get_first(
            "language.type/value[@lang='3']/text()"
        )
        if language is None or language_type is None:
            continue

        language_mapped = get_mapped_enum_value(language_code_enum_mapping, language)
        language_type_mapped = get_mapped_enum_value(
            language_usage_enum_mapping, language_type
        )

        if language_mapped is None or language_type_mapped is None:
            continue

        languages.append(
            efi.Language(
                code=language_mapped,
                usage=language_type_mapped,
            )
        )

    return languages
