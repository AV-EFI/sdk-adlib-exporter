from mappings.colour_type_enum import colour_type_enum
from records.base.base_record import BaseRecord
from records.base.utils import get_mapped_enum_value


def compute_has_colour_type(record: BaseRecord):
    colour = record.xml.get_first("colour_manifestation/value[@lang='3']/text()")

    if colour is None:
        return None

    return get_mapped_enum_value(colour_type_enum, colour)
