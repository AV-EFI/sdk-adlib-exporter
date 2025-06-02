from mappings.item_access_status_enum import item_access_status_enum
from records.base.base_record import BaseRecord
from records.base.utils import get_mapped_enum_value


def compute_has_access_status(record: BaseRecord):
    access_status = record.xml.get_first(
        "copy_status/value[@lang='3']/text()",
    )

    if access_status is None:
        return None

    return get_mapped_enum_value(item_access_status_enum, access_status)
