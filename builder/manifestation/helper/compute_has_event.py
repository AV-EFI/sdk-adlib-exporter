from avefi_schema import model as efi

from mappings.publication_event_type_enum_mapping import (
    publication_event_type_enum_mapping,
)


def compute_has_event(self):
    manifestationlevel_type_list = self.xml.xpath(
        "manifestationlevel_type/value[@lang='3']/text()"
    )

    if not manifestationlevel_type_list:
        return None

    manifestationlevel_type = manifestationlevel_type_list[0]

    if manifestationlevel_type not in publication_event_type_enum_mapping:
        raise Exception("No mapping found for key:", manifestationlevel_type)

    if publication_event_type_enum_mapping[manifestationlevel_type] is None:
        return

    return efi.PublicationEvent(
        type=publication_event_type_enum_mapping[manifestationlevel_type]
    )
