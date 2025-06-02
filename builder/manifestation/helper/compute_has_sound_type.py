from builder.base.base_builder import BaseBuilder
from builder.base.utils import get_mapped_enum_value
from mappings.sound_type_enum_mapping import sound_type_enum_mapping


def compute_has_sound_type(record: BaseBuilder):
    sound = record.xml.get_first("sound_manifestation/value[@lang='3']/text()")

    if sound is None:
        return None

    return get_mapped_enum_value(sound_type_enum_mapping, sound)
