from avefi_schema import model as efi

work_variant_type_enum_mapping = {
    "Monografisch": efi.WorkVariantTypeEnum.Monographic,
    "Komponente": efi.WorkVariantTypeEnum.Analytic,
    "Seriell": efi.WorkVariantTypeEnum.Serial,
}

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

language_code_enum_mapping = {
    "deutsch": efi.LanguageCodeEnum.deu,
    "japanisch": efi.LanguageCodeEnum.jpn,
    "englisch": efi.LanguageCodeEnum.eng,
    "rumänisch": efi.LanguageCodeEnum.rum,
    "französisch": efi.LanguageCodeEnum.fra,
    "tschechisch": efi.LanguageCodeEnum.cze,
    "italienisch": efi.LanguageCodeEnum.ita,
    "niederländisch": efi.LanguageCodeEnum.dut,
    "schwedisch": efi.LanguageCodeEnum.swe,
    "koreanisch": efi.LanguageCodeEnum.kor,
    "griechisch": efi.LanguageCodeEnum.grc,
    "russisch": efi.LanguageCodeEnum.rus,
    "spanisch": efi.LanguageCodeEnum.spa,
    "persisch": efi.LanguageCodeEnum.fas,
    "türkisch": efi.LanguageCodeEnum.tur,
    "portugiesisch": efi.LanguageCodeEnum.por,
    "norwegisch": efi.LanguageCodeEnum.nor,
    "hebräisch": efi.LanguageCodeEnum.heb,
    "romani": efi.LanguageCodeEnum.rom,
    "arabisch": efi.LanguageCodeEnum.ara,
    "ungarisch": efi.LanguageCodeEnum.hun,
    "chinesisch": efi.LanguageCodeEnum.chi,
    "litauisch": efi.LanguageCodeEnum.lit,
    "schweizerdeutsch": efi.LanguageCodeEnum.gsw,
    "bulgarisch": efi.LanguageCodeEnum.bul,
    "polnisch": efi.LanguageCodeEnum.pol,
    # NOT CORRECT ONLY TO PASS # NOT CORRECT ONLY TO PASS #
    "serbokroatisch": True,
    "belgisches Niederländisch": True,
    "hochchinesisch": True,
    "Original": True,
}


language_usage_enum_mapping = {
    "Zwischentitel": efi.LanguageUsageEnum.Intertitles,
    "Synchronfassung": efi.LanguageUsageEnum.Dubbed,
    "Dialog": efi.LanguageUsageEnum.SpokenLanguage,
    "Untertitel": efi.LanguageUsageEnum.Subtitles,
    "Voice-over": efi.LanguageUsageEnum.VoiceOver,
    "Vorspann": efi.LanguageUsageEnum.OpeningCredits,
    "Untertitel für Hörgeschädigte": efi.LanguageUsageEnum.SDHSubtitles,
    "Credits": efi.LanguageUsageEnum.ClosingCredits,
    "Audiodeskription für Blinde": efi.LanguageUsageEnum.AudioDescription,
    "Ohne Dialog": efi.LanguageUsageEnum.NoDialogue,
    # NOT CORRECT ONLY TO PASS # NOT CORRECT ONLY TO PASS #
    "OF": True,
    "OmU": True,
}
