from avefi_schema import model as efi

from records.base.base_record import BaseRecord
from records.base.helper.compute_described_by import compute_described_by
from records.base.helper.compute_has_identifier import compute_has_identifier
from records.work.helper.compute_has_event import compute_has_event
from records.work.helper.compute_has_form import compute_has_form
from records.work.helper.compute_has_genre import compute_has_genre
from records.work.helper.compute_has_subject import compute_has_subject
from records.work.helper.compute_is_part_of import compute_is_part_of
from records.work.helper.compute_same_as import compute_same_as
from records.work.helper.compute_title import (
    compute_has_primary_title,
    compute_has_alternative_title,
)
from records.work.helper.compute_type import compute_type


class WorkRecord(BaseRecord):

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
            has_alternative_title=compute_has_alternative_title(self),
            has_primary_title=compute_has_primary_title(self),
            has_identifier=compute_has_identifier(self),
        )
