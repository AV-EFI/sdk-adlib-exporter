from avefi_schema import model as efi

from records.base.base_record import BaseRecord


def compute_has_primary_title(record: BaseRecord):
    part_of_title = record.xml.get_first(
        "Part_of/part_of_reference/Part_of/part_of.title/text()",
    )

    part_of_lead_word = record.xml.get_first(
        "Part_of/part_of_reference/Part_of/part_of.lead_word/text()",
    )

    if part_of_lead_word is not None:
        title = part_of_lead_word + " " + part_of_title
    else:
        title = part_of_title

    return efi.Title(type=efi.TitleTypeEnum.TitleProper, has_name=title)
