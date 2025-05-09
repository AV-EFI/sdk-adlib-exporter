from avefi_schema import model as efi

directing_activity_type_enum = {
    "Regieassistenz": efi.DirectingActivityTypeEnum.AssistantDirector,
    "Casting": efi.DirectingActivityTypeEnum.CastingDirector,
    "Continuity": efi.DirectingActivityTypeEnum.Continuity,
    "Regie": efi.DirectingActivityTypeEnum.Director,
    "2nd Unit Regie": efi.DirectingActivityTypeEnum.SecondUnitDirector,
    "Stuntkoordination": efi.DirectingActivityTypeEnum.StuntArranger,
}
