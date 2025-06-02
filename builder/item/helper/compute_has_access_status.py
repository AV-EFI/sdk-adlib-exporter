from builder.base.utils import get_mapped_enum_value
from mappings.item_access_status_enum import item_access_status_enum


def compute_has_access_status(self):
    access_status_values = self.xml.xpath("copy_status/value[@lang='3']/text()")

    access_status = access_status_values[0] if access_status_values else None

    if access_status is None:
        return None

    return get_mapped_enum_value(item_access_status_enum, access_status)
