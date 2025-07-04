from avefi_schema import model as efi

from records.record import XMLAccessor
from records.utils import get_mapped_enum_value


def has_event(xml: XMLAccessor):
    manifestationlevel_type = xml.get_first(
        "manifestationlevel_type/value[@lang='3']/text()"
    )

    if manifestationlevel_type is None:
        return None

    manifestationlevel_type_mapped = get_mapped_enum_value(
        "PublicationEventTypeEnum", manifestationlevel_type
    )

    if manifestationlevel_type_mapped is None:
        return None

    return efi.PublicationEvent(type=manifestationlevel_type_mapped)
