from avefi_schema import model as efi

item_element_type_enum = {
    "Dupnegativ": efi.ItemElementTypeEnum.DuplicateNegative,
    "Duppositiv": efi.ItemElementTypeEnum.DuplicatePositive,
    "Bildnegativ": efi.ItemElementTypeEnum.ImageNegative,
    "Originalbildnegativ": efi.ItemElementTypeEnum.OriginalNegative,
    "Umkehrpositiv": efi.ItemElementTypeEnum.OriginalPositiveReversalFilm,
    "Positivkopie": efi.ItemElementTypeEnum.Positive,
    "Tonnegativ": efi.ItemElementTypeEnum.SoundNegative,
    # Covered keys without mapping! Please provide mapping! #
    "Positivkopie (kombiniert)": None,
    "Magnetband": None,
    "Umkehroriginal": None,
    "Umkehrkopie": None,
    "Dupnegativ (kombiniert)": None,
    "Color Reversal Intermediate": None,
    "Duppositiv (kombiniert)": None,
    "Uoc": None,
    "DAT": None,
    "Tonpositiv": None,
    "Umkehroriginal, kombiniert": None,
    "Umkehrkopie, kombiniert": None,
}
