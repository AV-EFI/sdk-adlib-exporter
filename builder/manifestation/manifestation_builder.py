from builder.base.base_builder import BaseBuilder
from avefi_schema import model as efi
from builder.manifestation.helper import *
from builder.base.helper import *


class ManifestationBuilder(BaseBuilder):
    def build(self):
        return efi.Manifestation(
            has_colour_type=None,
            has_item=None,
            has_sound_type=None,
            is_manifestation_of=compute_is_manifestation_of(self),
            same_as=None,
            has_duration=None,
            has_extent=None,
            has_format=None,
            has_note=None,
            has_webresource=None,
            described_by=compute_described_by(self),
            has_event=None,
            has_identifier=compute_has_identifier(self),
            in_language=compute_in_language(self),
            has_alternative_title=None,
            has_primary_title=compute_has_primary_title(self),
        )
