from avefi_schema import model as efi

from records.base.base_record import XMLAccessor


def compute_belongs_to(xml: XMLAccessor):
    part_of_list = xml.get_all("Part_of/part_of_reference.lref/text()")
    return [efi.LocalResource(id=priref) for priref in part_of_list]
