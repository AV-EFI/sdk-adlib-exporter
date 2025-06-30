from records.base.base_record import XMLAccessor
from records.base.helper.compute_belongs_to import compute_belongs_to


def compute_is_manifestation_of(xml: XMLAccessor):
    return compute_belongs_to(xml)
