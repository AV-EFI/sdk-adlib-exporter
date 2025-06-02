from avefi_schema import model as efi

from builder.base.base_builder import BaseBuilder


def compute_has_note(record: BaseBuilder):
    notes = record.xml.get_all(
        "Content_description/content.description/value[@lang='de-DE']/text()"
    )

    return [efi.TextArea(note) for note in notes]
