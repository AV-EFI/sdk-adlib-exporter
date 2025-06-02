from avefi_schema import model as efi

from builder.base.base_builder import BaseBuilder


def compute_same_as(record: BaseBuilder):
    # currently only generating "avefi:FilmportalResource"
    xml_alternative_numbers = record.xml.get_all("Alternative_number")

    for xml_alternative_number in xml_alternative_numbers:
        number = xml_alternative_number.get_first("alternative_number/text()")
        number_type = xml_alternative_number.get_first(
            "alternative_number.type/value/text()"
        )

        if number is None or number_type is None:
            continue

        if number_type == "ref_filmportal":
            return efi.FilmportalResource(id=number)

    return None
