from avefi_schema import model as efi

from builder.base.utils import UnresolvableReferenceError


def compute_belongs_to(self):
    part_of_list = self.xml.xpath("Part_of/part_of_reference.lref/text()")
    if part_of_list:
        for priref in part_of_list:
            if priref not in self.allowed_parents:
                raise UnresolvableReferenceError(f"{priref} not in parent records")
    return [efi.LocalResource(id=priref) for priref in part_of_list]
