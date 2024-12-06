from avefi_schema import model as efi

title_type_enum_mapping = {
    "Alternativtitel": efi.TitleTypeEnum.AlternativeTitle,
    "Originaltitel": efi.TitleTypeEnum.PreferredTitle,
    "Recherchehilfe": efi.TitleTypeEnum.SearchTitle,
    "Archivtitel": efi.TitleTypeEnum.SuppliedDevisedTitle,
    "Titelübersetzung": efi.TitleTypeEnum.TranslatedTitle,
    "Arbeitstitel": efi.TitleTypeEnum.WorkingTitle,
    # NOT CORRECT ONLY TO PASS # NOT CORRECT ONLY TO PASS #
    "Materialtitel": efi.TitleTypeEnum.AlternativeTitle,  # NOT CORRECT
    "Verleihtitel": efi.TitleTypeEnum.AlternativeTitle,  # NOT CORRECT
    "Schreibvariante": efi.TitleTypeEnum.AlternativeTitle,  # NOT CORRECT
    "Untertitel": efi.TitleTypeEnum.AlternativeTitle,  # NOT CORRECT
    "Displaytitel": efi.TitleTypeEnum.AlternativeTitle,  # NOT CORRECT
    "Reihentitel": efi.TitleTypeEnum.AlternativeTitle,  # NOT CORRECT
    "Abschnittstitel": efi.TitleTypeEnum.AlternativeTitle,  # NOT CORRECT
    "Fernsehtitel": efi.TitleTypeEnum.AlternativeTitle,  # NOT CORRECT
    "Serientitel": efi.TitleTypeEnum.AlternativeTitle,  # NOT CORRECT
    "Festivaltitel": efi.TitleTypeEnum.AlternativeTitle,  # NOT CORRECT
    "Episodentitel": efi.TitleTypeEnum.AlternativeTitle,  # NOT CORRECT
}
