from avefi_schema import model as efi

work_form_enum = {
    "Amateurfilm": efi.WorkFormEnum.AmateurFilm,
    "Kompilationsfilm": efi.WorkFormEnum.Compilation,
    "Home movie": efi.WorkFormEnum.HomeMovie,
    "Kurzfilm": efi.WorkFormEnum.Short,
    "Trailer": efi.WorkFormEnum.Trailer,
    "Episodenfilm": efi.WorkFormEnum.AnthologyFilm,
    "Werbefilm": efi.WorkFormEnum.Commercial,
    "Lehr-/Unterrichtsfilm": efi.WorkFormEnum.EducationalFilm,
    "Essayfilm": efi.WorkFormEnum.EssayFilm,
    "Experimentalfilm": efi.WorkFormEnum.ExperimentalFilm,
    "Industrie-/Wirtschaftsfilm": efi.WorkFormEnum.IndustrialFilm,
    "Musikvideo": efi.WorkFormEnum.MusicVideo,
    "Wochenschau": efi.WorkFormEnum.Newsreel,
    # Covered keys without mapping! Please provide mapping! #
    "Spielfilm": None,
    "Dokumentarfilm": None,
    "Dokumentarfilm mit Spielhandlung": None,
    "Dokumentation": None,
    "Animation": None,
    "Reportage": None,
    "Musiksendung": None,
    "Propagandafilm": None,
}
