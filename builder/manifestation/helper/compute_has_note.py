# currently only retrieving german notes, to change remove "[@lang='de-DE']"

from avefi_schema import model as efi


def compute_has_note(self):
    notes_list = self.xml.xpath(
        "Content_description/content.description/value[@lang='de-DE']/text()"
    )

    return [efi.TextArea(note) for note in notes_list]
