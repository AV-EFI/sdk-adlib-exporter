from mappings.frame_rate_enum import frame_rate_enum
from records.base.base_record import BaseRecord
from records.base.utils import get_mapped_enum_value


def compute_has_frame_rate(record: BaseRecord):
    frame_rate = record.xml.get_first(
        "Film_speed/frame_rate/value[@lang='de-DE']/text()"
    )

    if frame_rate is None:
        return None

    return get_mapped_enum_value(frame_rate_enum, frame_rate)
