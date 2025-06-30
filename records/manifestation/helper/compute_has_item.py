from avefi_schema import model as efi

from records.base.base_record import XMLAccessor


def compute_has_item(xml: XMLAccessor):
    prirefs = xml.get_all("Parts/parts.reference.lref/text()")

    return [efi.LocalResource(id=priref) for priref in prirefs]
