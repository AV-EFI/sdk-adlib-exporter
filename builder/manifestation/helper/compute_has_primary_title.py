from avefi_schema import model as efi


def compute_has_primary_title(self):
    title_list = self.xml.xpath("Title/title/text()")
    title_article_list = self.xml.xpath("Title/title.article/text()")

    try:
        if title_list:
            title = (
                title_list[0]
                if not title_article_list
                else title_article_list[0] + " " + title_list[0]
            )
        else:
            part_of_title_list = self.xml.xpath("Part_of/part_of.title/text()")
            part_of_lead_word_list = self.xml.xpath("Part_of/part_of.lead_word/text()")
            if part_of_lead_word_list:
                title = part_of_lead_word_list[0] + " " + part_of_title_list[0]
            else:
                title = part_of_title_list[0]

    except IndexError as e:
        raise Exception("Problem with has_primary_title:", e)

    return efi.Title(type=efi.TitleTypeEnum.PreferredTitle, has_name=title)
