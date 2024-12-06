from avefi_schema import model as efi

work_variant_type_enum_mapping = {
    "Monografisch": efi.WorkVariantTypeEnum.Monographic,
    "Komponente": efi.WorkVariantTypeEnum.Analytic,
    "Seriell": efi.WorkVariantTypeEnum.Serial,
}
