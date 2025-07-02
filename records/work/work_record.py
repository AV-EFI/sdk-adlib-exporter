from avefi_schema import model as efi

from records.base.base_record import BaseRecord
from records.base.helper.compute_described_by import compute_described_by
from records.base.helper.compute_has_identifier import compute_has_identifier
from records.base.utils import simple_remap
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


class WorkRecord(BaseRecord):

    def build(self):
        return efi.WorkVariant(
            has_form=compute_has_form(self.xml),
            has_genre=compute_has_genre(self.xml),
            has_subject=compute_has_subject(self.xml),
            is_part_of=compute_is_part_of(self.xml),
            is_variant_of=None,
            same_as=compute_same_as(self.xml),
            variant_type=None,
            described_by=compute_described_by(self.xml),
            has_event=compute_has_event(self.xml),
            has_alternative_title=compute_has_alternative_title(self.xml),
            has_primary_title=compute_has_primary_title(self.xml),
            has_identifier=compute_has_identifier(self.xml),
            type=simple_remap(
                self.xml,
                "work.description_type/value[@lang='3']/text()",
                "WorkVariantTypeEnum",
            ),
        )
