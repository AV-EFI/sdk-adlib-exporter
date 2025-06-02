from avefi_schema import model as efi

from builder.base.base_builder import BaseBuilder
from builder.base.utils import get_mapped_enum_value
from mappings.publication_event_type_enum_mapping import (
    publication_event_type_enum_mapping,
)


def compute_has_event(record: BaseBuilder):
    manifestationlevel_type = record.xml.get_first(
        "manifestationlevel_type/value[@lang='3']/text()"
    )

    if manifestationlevel_type is None:
        return None

    manifestationlevel_type_mapped = get_mapped_enum_value(
        publication_event_type_enum_mapping, manifestationlevel_type
    )

    if manifestationlevel_type_mapped is None:
        return None

    return efi.PublicationEvent(type=manifestationlevel_type_mapped)
