from avefi_schema import model as efi

from records.base.base_record import BaseRecord
from records.base.helper.compute_described_by import compute_described_by
from records.base.helper.compute_has_duration import compute_has_duration
from records.base.helper.compute_has_extent import compute_has_extent
from records.base.helper.compute_has_identifier import compute_has_identifier
from records.base.helper.compute_in_language import compute_in_language
from records.item.helper.compute_element_type import compute_element_type
from records.item.helper.compute_has_access_status import compute_has_access_status
from records.item.helper.compute_has_colour_type import compute_has_colour_type
from records.item.helper.compute_has_format import compute_has_format
from records.item.helper.compute_has_frame_rate import compute_has_frame_rate
from records.item.helper.compute_has_primary_title import compute_has_primary_title
from records.item.helper.compute_has_webresource import compute_has_webresource
from records.item.helper.compute_is_item_of import compute_is_item_of


class ItemRecord(BaseRecord):

    def build(self):
        return efi.Item(
            element_type=compute_element_type(self),
            has_access_status=compute_has_access_status(self),
            is_copy_of=None,  # will not be implemented
            is_derivative_of=None,  # will not be implemented
            is_item_of=compute_is_item_of(self),
            has_duration=compute_has_duration(self),
            has_extent=compute_has_extent(self),
            has_format=compute_has_format(self),
            has_note=None,  # will not be implemented
            has_webresource=compute_has_webresource(self),
            described_by=compute_described_by(self),
            has_event=None,  # Todo
            has_identifier=compute_has_identifier(self),
            in_language=compute_in_language(self),
            has_alternative_title=None,
            has_primary_title=compute_has_primary_title(self),
            has_frame_rate=compute_has_frame_rate(self),
            has_colour_type=compute_has_colour_type(self),
        )
