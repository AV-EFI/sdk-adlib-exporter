from avefi_schema import model as efi

from builder.base.base_builder import BaseBuilder
from builder.base.helper.compute_described_by import compute_described_by
from builder.base.helper.compute_has_duration import compute_has_duration
from builder.base.helper.compute_has_extent import compute_has_extent
from builder.base.helper.compute_has_identifier import compute_has_identifier
from builder.base.helper.compute_in_language import compute_in_language
from builder.item.helper.compute_element_type import compute_element_type
from builder.item.helper.compute_has_primary_title import compute_has_primary_title
from builder.item.helper.compute_has_webresource import compute_has_webresource
from builder.item.helper.compute_is_item_of import compute_is_item_of


class ItemBuilder(BaseBuilder):

    def build(self):
        return efi.Item(
            element_type=compute_element_type(self),
            has_access_status=None,  # Todo
            is_copy_of=None,  # will not be implemented
            is_derivative_of=None,  # will not be implemented
            is_item_of=compute_is_item_of(self),
            has_duration=compute_has_duration(self),
            has_extent=compute_has_extent(self),
            has_format=None,  # Todo
            has_note=None,  # will not be implemented
            has_webresource=compute_has_webresource(self),
            described_by=compute_described_by(self),
            has_event=None,  # Todo
            has_identifier=compute_has_identifier(self),
            in_language=compute_in_language(self),
            has_alternative_title=None,
            has_primary_title=compute_has_primary_title(self),
        )
