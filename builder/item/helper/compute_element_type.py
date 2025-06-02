from builder.base.base_builder import BaseBuilder
from builder.base.utils import get_mapped_enum_value
from mappings.item_element_type_enum_mapping import item_element_type_enum_mapping


def compute_element_type(record: BaseBuilder):
    element_type = record.xml.get_first(
        "mat_characteristics/mat_characteristics.material_type_film/value[@lang='de-DE']/text()",
    )

    if element_type is None:
        return None

    return get_mapped_enum_value(item_element_type_enum_mapping, element_type)
