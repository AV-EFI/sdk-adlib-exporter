from avefi_schema import model as efi

from builder.base.base_builder import BaseBuilder


def compute_has_item(record: BaseBuilder):
    prirefs = record.xml.get_all("Parts/parts.reference.lref/text()")

    return [efi.LocalResource(id=priref) for priref in prirefs]
