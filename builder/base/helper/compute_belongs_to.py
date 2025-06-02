from avefi_schema import model as efi

from builder.base.base_builder import BaseBuilder
from builder.base.custom_errors import UnresolvableReferenceError


def compute_belongs_to(record: BaseBuilder):
    part_of_list = record.xml.get_all("Part_of/part_of_reference.lref/text()")
    if part_of_list:
        for priref in part_of_list:
            if priref not in record.allowed_parents:
                raise UnresolvableReferenceError(f"{priref} not in parent records")
    return [efi.LocalResource(id=priref) for priref in part_of_list]
