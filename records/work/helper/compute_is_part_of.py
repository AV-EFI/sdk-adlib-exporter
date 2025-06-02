from records.base.base_record import BaseRecord
from records.base.helper.compute_belongs_to import compute_belongs_to


def compute_is_part_of(record: BaseRecord):
    return compute_belongs_to(record)
