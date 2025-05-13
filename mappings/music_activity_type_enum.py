from avefi_schema import model as efi

music_activity_type_enum = {
    "Choreografie": efi.MusicActivityTypeEnum.Choreographer,
    "Musik (Credit)": efi.MusicActivityTypeEnum.Composer,
    "Arrangeur": efi.MusicActivityTypeEnum.MusicArranger,
    "Dirigent; Dirigentin": efi.MusicActivityTypeEnum.MusicConductor,
    "Gesang": efi.MusicActivityTypeEnum.SingingVoice,
    "Komponist; Komponistin": efi.MusicActivityTypeEnum.SongComposer,
}
