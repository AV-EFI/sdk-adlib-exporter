from builder.base.base_builder import BaseBuilder
from builder.base.helper.compute_belongs_to import compute_belongs_to


def compute_is_manifestation_of(record: BaseBuilder):
    return compute_belongs_to(record)
