from mappings.item_element_type_enum import item_element_type_enum
from records.base.base_record import BaseRecord
from records.base.utils import get_mapped_enum_value


def compute_element_type(record: BaseRecord):
    element_type = record.xml.get_first(
        "mat_characteristics/mat_characteristics.material_type_film/value[@lang='de-DE']/text()",
    )

    if element_type is None:
        return None

    return get_mapped_enum_value(item_element_type_enum, element_type)
