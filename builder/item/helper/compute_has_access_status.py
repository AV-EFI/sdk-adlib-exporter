from builder.base.base_builder import BaseBuilder
from builder.base.utils import get_mapped_enum_value
from mappings.item_access_status_enum import item_access_status_enum


def compute_has_access_status(record: BaseBuilder):
    access_status = record.xml.get_first(
        "copy_status/value[@lang='3']/text()",
    )

    if access_status is None:
        return None

    return get_mapped_enum_value(item_access_status_enum, access_status)
