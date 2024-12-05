from avefi_schema import model as efi


def compute_has_primary_title(self):
    part_of_title_list = self.xml.xpath(
        "Part_of/part_of_reference/Part_of/part_of.title/text()"
    )
    part_of_lead_word_list = self.xml.xpath(
        "Part_of/part_of_reference/Part_of/part_of.lead_word/text()"
    )

    try:
        # Found Multiple Cases where there was more than one Part_of entry, currently choosing only the first!
        if part_of_lead_word_list:
            title = part_of_lead_word_list[0] + " " + part_of_title_list[0]
        else:
            title = part_of_title_list[0]

    except IndexError as e:
        raise Exception("Problem with has_primary_title:", e)

    return efi.Title(type=efi.TitleTypeEnum.TitleProper, has_name=title)
