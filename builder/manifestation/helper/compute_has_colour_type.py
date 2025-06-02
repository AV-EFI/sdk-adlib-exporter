from builder.base.base_builder import BaseBuilder
from builder.base.utils import get_mapped_enum_value
from mappings.colour_type_enum_mapping import colour_type_enum_mapping


def compute_has_colour_type(record: BaseBuilder):
    colour = record.xml.get_first("colour_manifestation/value[@lang='3']/text()")

    if colour is None:
        return None

    return get_mapped_enum_value(colour_type_enum_mapping, colour)
