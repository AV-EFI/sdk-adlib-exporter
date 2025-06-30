from avefi_schema import model as efi

from mappings.format_digital_file_type_enum import format_digital_file_type_enum
from mappings.format_film_type_enum import format_film_type_enum
from mappings.format_optical_type_enum import format_optical_type_enum
from mappings.format_video_type_enum import format_video_type_enum
from records.base.base_record import XMLAccessor
from records.base.utils import get_mapped_enum_value


def compute_has_format(xml: XMLAccessor):
    formats = []

    for format_class, xpath, enum, name in [
        (
            efi.DigitalFile,
            "file_type/value[@lang='de-DE']/text()",
            format_digital_file_type_enum,
            "format_digital_file_type_enum",
        ),
        (
            efi.Film,
            "mat_characteristics/mat_characteristics.material_format_film/value[@lang='de-DE']/text()",
            format_film_type_enum,
            "format_film_type_enum",
        ),
        (
            efi.Optical,
            "material_type_digitalvideo/value[@lang='de-DE']/text()",
            format_optical_type_enum,
            "format_optical_type_enum",
        ),
        (
            efi.Video,
            "material_type_video/value[@lang='de-DE']/text()",
            format_video_type_enum,
            "format_video_type_enum",
        ),
        (
            efi.Video,
            "material_type_digitalvideo/value[@lang='de-DE']/text()",
            format_video_type_enum,
            "format_video_type_enum",
        ),
    ]:
        value = xml.get_first(xpath)

        if value is None:
            continue

        mapped_value = get_mapped_enum_value(enum, value, name=name)

        if mapped_value is None:
            continue

        formats.append(format_class(type=mapped_value))

    return formats
