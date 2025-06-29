from avefi_schema import model as efi

from mappings.colour_type_enum import colour_type_enum
from mappings.frame_rate_enum import frame_rate_enum
from mappings.item_access_status_enum import item_access_status_enum
from mappings.item_element_type_enum import item_element_type_enum
from mappings.sound_type_enum import sound_type_enum
from records.base.base_record import BaseRecord
from records.base.helper.compute_described_by import compute_described_by
from records.base.helper.compute_has_duration import compute_has_duration
from records.base.helper.compute_has_extent import compute_has_extent
from records.base.helper.compute_has_identifier import compute_has_identifier
from records.base.helper.compute_in_language import compute_in_language
from records.base.utils import simple_remap
from records.item.helper.compute_has_format import compute_has_format
from records.item.helper.compute_has_primary_title import compute_has_primary_title
from records.item.helper.compute_has_webresource import compute_has_webresource
from records.item.helper.compute_is_item_of import compute_is_item_of


class ItemRecord(BaseRecord):

    def build(self):
        return efi.Item(
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
            element_type=simple_remap(
                self,
                "mat_characteristics/mat_characteristics.material_type_film/value[@lang='de-DE']/text()",
                item_element_type_enum,
            ),
            has_access_status=simple_remap(
                self,
                "copy_status/value[@lang='3']/text()",
                item_access_status_enum,
            ),
            has_frame_rate=simple_remap(
                self,
                "Film_speed/frame_rate/value[@lang='de-DE']/text()",
                frame_rate_enum,
            ),
            has_colour_type=simple_remap(
                self,
                "colour_type/value[@lang='3']/text()",
                colour_type_enum,
            ),
            has_sound_type=simple_remap(
                self,
                "sound_item/value[@lang='de-DE']/text()",
                sound_type_enum,
            ),
        )
