from avefi_schema import model as efi

sound_type_enum = {
    "Mute": efi.SoundTypeEnum.Mute,
    "Stumm": efi.SoundTypeEnum.Silent,
    "Ton": efi.SoundTypeEnum.Sound,
}
