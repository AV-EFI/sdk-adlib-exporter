from avefi_schema import model as efi

title_type_enum_mapping = {
    "Alternativtitel": efi.TitleTypeEnum.AlternativeTitle,
    "Originaltitel": efi.TitleTypeEnum.PreferredTitle,
    "Recherchehilfe": efi.TitleTypeEnum.SearchTitle,
    "Archivtitel": efi.TitleTypeEnum.SuppliedDevisedTitle,
    "Titelübersetzung": efi.TitleTypeEnum.TranslatedTitle,
    "Arbeitstitel": efi.TitleTypeEnum.WorkingTitle,
    # Covered keys without mapping! Please provide mapping! #
    "Materialtitel": None,
    "Verleihtitel": None,
    "Schreibvariante": None,
    "Untertitel": None,
    "Displaytitel": None,
    "Reihentitel": None,
    "Abschnittstitel": None,
    "Fernsehtitel": None,
    "Serientitel": None,
    "Festivaltitel": None,
    "Episodentitel": None,
}
