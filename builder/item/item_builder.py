from builder.base.base_builder import BaseBuilder
from avefi_schema import model as efi
from builder.item.helper import *
from builder.base.helper import *


class ItemBuilder(BaseBuilder):

    def build(self):
        return efi.Item(
            element_type=compute_element_type(self),
            has_access_status=None,
            is_copy_of=None,
            is_derivative_of=None,
            is_item_of=compute_is_item_of(self),
            has_duration=None,
            has_extent=None,
            has_format=None,
            has_note=None,
            has_webresource=compute_has_webresource(self),
            described_by=compute_described_by(self),
            has_event=None,
            has_identifier=compute_has_identifier(self),
            in_language=compute_in_language(self),
            has_alternative_title=None,
            has_primary_title=compute_has_primary_title(self),
        )
