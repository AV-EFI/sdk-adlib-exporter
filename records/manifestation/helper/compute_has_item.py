from avefi_schema import model as efi

from records.base.base_record import BaseRecord


def compute_has_item(record: BaseRecord):
    prirefs = record.xml.get_all("Parts/parts.reference.lref/text()")

    return [efi.LocalResource(id=priref) for priref in prirefs]
