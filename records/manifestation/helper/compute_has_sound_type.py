from mappings.sound_type_enum import sound_type_enum
from records.base.base_record import BaseRecord
from records.base.utils import get_mapped_enum_value


def compute_has_sound_type(record: BaseRecord):
    sound = record.xml.get_first("sound_manifestation/value[@lang='3']/text()")

    if sound is None:
        return None

    return get_mapped_enum_value(sound_type_enum, sound)
