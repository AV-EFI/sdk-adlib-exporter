from avefi_schema import model as efi

from records.base.base_record import BaseRecord


def compute_has_primary_title(record: BaseRecord):
    title = record.xml.get_first("Title/title/text()")

    title_article = record.xml.get_first("Title/title.article/text()")

    if title is not None:
        title = title if not title_article else title_article + " " + title
    else:
        part_of_title = record.xml.get_first("Part_of/part_of.title/text()")
        part_of_lead_word = record.xml.get_first("Part_of/part_of.lead_word/text()")
        if part_of_lead_word is not None:
            title = part_of_lead_word + " " + part_of_title
        else:
            title = part_of_title

    return efi.Title(type=efi.TitleTypeEnum.PreferredTitle, has_name=title)
