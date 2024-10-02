from builder.base_builder import BaseBuilder
from avefi_schema import model as efi


class ManifestationBuilder(BaseBuilder):

    def build(self):
        return efi.Manifestation(
            has_identifier=super().has_identifier,
            is_manifestation_of=self.is_manifestation_of,
            has_primary_title=self.has_primary_title,
            described_by=super().described_by,
            in_language=super().in_language,
        )

    @property
    def is_manifestation_of(self):
        return super().belongs_to

    @property
    def has_primary_title(self):
        title_list = self.xml.xpath("Title/title/text()")
        part_of_title_list = self.xml.xpath("Part_of/part_of.title/text()")
        part_of_lead_word_list = self.xml.xpath("Part_of/part_of.lead_word/text()")

        try:
            if title_list:
                title = title_list[0]
            else:
                # Found 2 Cases where there was more than one Part_of entry, currently choosing only the first!
                if part_of_lead_word_list:
                    title = part_of_lead_word_list[0] + " " + part_of_title_list[0]
                else:
                    title = part_of_title_list[0]

        except IndexError as e:
            raise Exception("Problem with has_primary_title:", e)

        return efi.Title(type=efi.TitleTypeEnum.TitleProper, has_name=title)
