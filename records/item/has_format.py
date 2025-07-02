from avefi_schema import model as efi

from records.record import XMLAccessor
from records.utils import get_mapped_enum_value


def has_format(xml: XMLAccessor):
    formats = []

    for format_class, xpath, enum_name in [
        (
            efi.DigitalFile,
            "file_type/value[@lang='de-DE']/text()",
            "FormatDigitalFileTypeEnum",
        ),
        (
            efi.Film,
            "mat_characteristics/mat_characteristics.material_format_film/value[@lang='de-DE']/text()",
            "FormatFilmTypeEnum",
        ),
        (
            efi.Optical,
            "material_type_digitalvideo/value[@lang='de-DE']/text()",
            "FormatOpticalTypeEnum",
        ),
        (
            efi.Video,
            "material_type_video/value[@lang='de-DE']/text()",
            "FormatVideoTypeEnum",
        ),
        (
            efi.Video,
            "material_type_digitalvideo/value[@lang='de-DE']/text()",
            "FormatVideoTypeEnum",
        ),
    ]:
        value = xml.get_first(xpath)

        if value is None:
            continue

        mapped_value = get_mapped_enum_value(enum_name, value)

        if mapped_value is None:
            continue

        formats.append(format_class(type=mapped_value))

    return formats
