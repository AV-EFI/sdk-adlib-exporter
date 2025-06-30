from avefi_schema import model as efi

from mappings.colour_type_enum import colour_type_enum
from mappings.sound_type_enum import sound_type_enum
from records.base.base_record import BaseRecord
from records.base.helper.compute_described_by import compute_described_by
from records.base.helper.compute_has_duration import compute_has_duration
from records.base.helper.compute_has_extent import compute_has_extent
from records.base.helper.compute_has_identifier import compute_has_identifier
from records.base.helper.compute_in_language import compute_in_language
from records.base.utils import simple_remap
from records.manifestation.helper.compute_has_event import compute_has_event
from records.manifestation.helper.compute_has_item import compute_has_item
from records.manifestation.helper.compute_has_note import compute_has_note
from records.manifestation.helper.compute_has_primary_title import (
    compute_has_primary_title,
)
from records.manifestation.helper.compute_is_manifestation_of import (
    compute_is_manifestation_of,
)


class ManifestationRecord(BaseRecord):
    def build(self):
        return efi.Manifestation(
            has_item=compute_has_item(self.xml),
            is_manifestation_of=compute_is_manifestation_of(self.xml),
            same_as=None,  # will not be implemented
            has_duration=compute_has_duration(self.xml),
            has_extent=compute_has_extent(self.xml),
            has_format=None,  # will not be implemented
            has_note=compute_has_note(self.xml),
            has_webresource=None,  # will not be implemented
            described_by=compute_described_by(self.xml),
            has_event=compute_has_event(self.xml),
            has_identifier=compute_has_identifier(self.xml),
            in_language=compute_in_language(self.xml),
            has_alternative_title=None,
            has_primary_title=compute_has_primary_title(self.xml),
            has_colour_type=simple_remap(
                self.xml,
                "colour_manifestation/value[@lang='3']/text()",
                colour_type_enum,
            ),
            has_sound_type=simple_remap(
                self.xml,
                "sound_manifestation/value[@lang='3']/text()",
                sound_type_enum,
            ),
        )
