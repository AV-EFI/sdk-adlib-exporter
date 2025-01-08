from avefi_schema import model as efi

colour_type_enum_mapping = {
    "schwarz-weiß": efi.ColourTypeEnum.BlackAndWhite,
    "Farbe": efi.ColourTypeEnum.Colour,
    "Farbe und schwarz-weiß": efi.ColourTypeEnum.ColourBlackAndWhite,
}
