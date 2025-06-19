from avefi_schema import model as efi

language_usage_enum = {
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
    # Covered keys without mapping! Please provide mapping! #
    "OF": None,
    "OmU": None,
}
