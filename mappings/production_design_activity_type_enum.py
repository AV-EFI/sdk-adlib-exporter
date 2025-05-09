from avefi_schema import model as efi

production_design_activity_type_enum = {
    "Ausstattung": efi.ProductionDesignActivityTypeEnum.ArtDirector,
    "Ausstattungsassistenz": efi.ProductionDesignActivityTypeEnum.AssistantArtDirector,
    "Kostümbild": efi.ProductionDesignActivityTypeEnum.CostumeDesigner,
    "Garderobier": efi.ProductionDesignActivityTypeEnum.Costumer,
    "Garderobe (Credit)": efi.ProductionDesignActivityTypeEnum.Gowns,
    "Maske (Credit)": efi.ProductionDesignActivityTypeEnum.MakeUpArtist,
    "Production Design": efi.ProductionDesignActivityTypeEnum.ProductionDesigner,
    "Requisite": efi.ProductionDesignActivityTypeEnum.PropertyMaster,
    "Kulissenmaler": efi.ProductionDesignActivityTypeEnum.ScenicArtist,
    "Innenrequisite": efi.ProductionDesignActivityTypeEnum.SetDecorator,
    "Set Design": efi.ProductionDesignActivityTypeEnum.SetDesigner,
    "Storyboard": efi.ProductionDesignActivityTypeEnum.StoryboardArtist,
    "Titeldesign": efi.ProductionDesignActivityTypeEnum.TitleDesigner,
}
