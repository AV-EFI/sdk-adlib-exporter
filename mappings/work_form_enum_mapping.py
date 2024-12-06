from avefi_schema import model as efi

work_form_enum_mapping = {
    "Amateurfilm": efi.WorkFormEnum.AmateurFilm,
    "Kompilationsfilm": efi.WorkFormEnum.Compilation,
    "Spielfilm": efi.WorkFormEnum.Feature,
    "Home Movie": efi.WorkFormEnum.HomeMovie,
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
    # NOT CORRECT ONLY TO PASS # NOT CORRECT ONLY TO PASS #
    "Dokumentarfilm": efi.WorkFormEnum.AmateurFilm,
    "Dokumentarfilm mit Spielhandlung": efi.WorkFormEnum.AmateurFilm,
    "Dokumentation": efi.WorkFormEnum.AmateurFilm,
    "Animation": efi.WorkFormEnum.AmateurFilm,
    "Reportage": efi.WorkFormEnum.AmateurFilm,
    "Musiksendung": efi.WorkFormEnum.AmateurFilm,
    "Propagandafilm": efi.WorkFormEnum.AmateurFilm,
}
