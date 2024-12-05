from builder.base.base_builder import BaseBuilder
from avefi_schema import model as efi
from builder.manifestation.helper.compute_has_primary_title import (
    compute_has_primary_title,
)
from builder.manifestation.helper.compute_is_manifestation_of import (
    compute_is_manifestation_of,
)
from builder.base.helper.compute_has_identifier import compute_has_identifier
from builder.base.helper.compute_described_by import compute_described_by
from builder.base.helper.compute_in_language import compute_in_language


class ManifestationBuilder(BaseBuilder):
    def build(self):
        return efi.Manifestation(
            has_identifier=compute_has_identifier(self),
            is_manifestation_of=compute_is_manifestation_of(self),
            has_primary_title=compute_has_primary_title(self),
            described_by=compute_described_by(self),
            in_language=compute_in_language(self),
        )
