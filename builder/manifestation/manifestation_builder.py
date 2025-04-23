from avefi_schema import model as efi

from builder.base.base_builder import BaseBuilder
from builder.base.helper.compute_described_by import compute_described_by
from builder.base.helper.compute_has_duration import compute_has_duration
from builder.base.helper.compute_has_extent import compute_has_extent
from builder.base.helper.compute_has_identifier import compute_has_identifier
from builder.base.helper.compute_in_language import compute_in_language
from builder.manifestation.helper.compute_has_colour_type import compute_has_colour_type
from builder.manifestation.helper.compute_has_item import compute_has_item
from builder.manifestation.helper.compute_has_note import compute_has_note
from builder.manifestation.helper.compute_has_primary_title import (
    compute_has_primary_title,
)
from builder.manifestation.helper.compute_has_sound_type import compute_has_sound_type
from builder.manifestation.helper.compute_is_manifestation_of import (
    compute_is_manifestation_of,
)


class ManifestationBuilder(BaseBuilder):
    def build(self):
        return efi.Manifestation(
            has_colour_type=compute_has_colour_type(self),
            has_item=compute_has_item(self),
            has_sound_type=compute_has_sound_type(self),
            is_manifestation_of=compute_is_manifestation_of(self),
            same_as=None,  # will not be implemented
            has_duration=compute_has_duration(self),
            has_extent=compute_has_extent(self),
            has_format=None,  # will not be implemented
            has_note=compute_has_note(self),
            has_webresource=None,  # will not be implemented
            described_by=compute_described_by(self),
            # has_event=None,  # Todo
            has_identifier=compute_has_identifier(self),
            in_language=compute_in_language(self),
            has_alternative_title=None,
            has_primary_title=compute_has_primary_title(self),
        )
