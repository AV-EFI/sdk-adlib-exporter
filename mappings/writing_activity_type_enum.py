from avefi_schema import model as efi

writing_activity_type_enum = {
    "Adaption": efi.WritingActivityTypeEnum.Adaptation,
    "Idee": efi.WritingActivityTypeEnum.Idea,
    "Buch (Literaturvorlage)": efi.WritingActivityTypeEnum.SourceMaterial,
    "Inszenierung": efi.WritingActivityTypeEnum.Stagedby,
    "Drehbuch": efi.WritingActivityTypeEnum.Writer,
}
