from avefi_schema import model as efi

format_film_type_enum = {
    "16mm": efi.FormatFilmTypeEnum["16mmFilm"],
    "17,5mm": efi.FormatFilmTypeEnum["17.5mmFilm"],
    "35mm": efi.FormatFilmTypeEnum["35mmFilm"],
    "70mm": efi.FormatFilmTypeEnum["70mmFilm"],
    "8mm": efi.FormatFilmTypeEnum["8mmFilm"],
    "9,5mm": efi.FormatFilmTypeEnum["9.5mmFilm"],
    "S16mm": efi.FormatFilmTypeEnum.Super16mmFilm,
    "S8mm": efi.FormatFilmTypeEnum.Super8mmFilm,
    # Covered keys without mapping! Please provide mapping! #
    "6,35mm": None,
    "16, 35": None,
    "35 + 16": None,
    "8 + 16": None,
    "DAT": None,
    "DTRS": None,
}
