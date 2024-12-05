from builder.work.helper import *
from builder.base.helper import *
from builder.base.base_builder import BaseBuilder
from avefi_schema import model as efi


class WorkBuilder(BaseBuilder):

    def build(self):
        return efi.WorkVariant(
            has_form=compute_has_form(self),
            has_genre=compute_has_genre(self),
            has_subject=compute_has_subject(self),
            is_part_of=compute_is_part_of(self),
            is_variant_of=None,
            same_as=compute_same_as(self),
            type=compute_type(self),
            variant_type=None,
            described_by=compute_described_by(self),
            has_event=compute_has_event(self),
            in_language=None,
            has_alternative_title=compute_has_alternative_title(self),
            has_primary_title=compute_has_primary_title(self),
            has_identifier=compute_has_identifier(self),
        )
