from avefi_schema import model as efi

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
            is_item_of=compute_is_item_of(self.xml),
            has_duration=compute_has_duration(self.xml),
            has_extent=compute_has_extent(self.xml),
            has_format=compute_has_format(self.xml),
            has_note=None,  # will not be implemented
            has_webresource=compute_has_webresource(self.xml),
            described_by=compute_described_by(self.xml),
            has_event=None,  # Todo
            has_identifier=compute_has_identifier(self.xml),
            in_language=compute_in_language(self.xml),
            has_alternative_title=None,
            has_primary_title=compute_has_primary_title(self.xml),
            element_type=simple_remap(
                self.xml,
                "mat_characteristics/mat_characteristics.material_type_film/value[@lang='de-DE']/text()",
                "ItemElementTypeEnum",
            ),
            has_access_status=simple_remap(
                self.xml,
                "copy_status/value[@lang='3']/text()",
                "ItemAccessStatusEnum",
            ),
            has_frame_rate=simple_remap(
                self.xml,
                "Film_speed/frame_rate/value[@lang='de-DE']/text()",
                "FrameRateEnum",
            ),
            has_colour_type=simple_remap(
                self.xml,
                "colour_type/value[@lang='3']/text()",
                "ColourTypeEnum",
            ),
            has_sound_type=simple_remap(
                self.xml,
                "sound_item/value[@lang='de-DE']/text()",
                "SoundTypeEnum",
            ),
        )
