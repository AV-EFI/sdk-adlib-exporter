from builder.base_builder import BaseBuilder
from avefi_schema import model as efi


class ItemBuilder(BaseBuilder):

    def build(self):
        return efi.Item(
            has_identifier=super().has_identifier,
            is_item_of=self.is_item_of,
            has_primary_title=self.has_primary_title,
            has_webresource=self.has_webresource,
            described_by=super().described_by,
            in_language=super().in_language,
        )

    @property
    def is_item_of(self):
        return super().belongs_to[0]

    @property
    def has_primary_title(self):
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

    @property
    def has_webresource(self):
        uri = (
            "https://sammlungen.deutsche-kinemathek.de/recherche/itemdetails/sdk"
            + self.xml.xpath("priref/text()")[0]
        )
        return efi.HttpUri(uri)
