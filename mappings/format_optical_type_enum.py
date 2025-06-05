from avefi_schema import model as efi

format_optical_type_enum = {
    "Blu-ray": efi.FormatOpticalTypeEnum.BluRay,
    "CD": efi.FormatOpticalTypeEnum.CD,
    "DVD": efi.FormatOpticalTypeEnum.DVD,
    # Covered keys without mapping! Please provide mapping! #
    "DigiBeta": None,
    "HDCam SR": None,
    "HDCam": None,
}
