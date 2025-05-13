from avefi_schema import model as efi

producing_activity_type_enum = {
    "Associate Producer": efi.ProducingActivityTypeEnum.AssociateProducer,
    "Executive Producer": efi.ProducingActivityTypeEnum.ExecutiveProducer,
    "Herstellungsleitung": efi.ProducingActivityTypeEnum.LineProducer,
    "Location Scout": efi.ProducingActivityTypeEnum.LocationManager,
    "Produktion (Credit)": efi.ProducingActivityTypeEnum.Producer,
    "Produktionsassistenz": efi.ProducingActivityTypeEnum.ProductionAssistant,
    "Produktionskoordination": efi.ProducingActivityTypeEnum.ProductionCoordinator,
    "Aufnahmeleitung": efi.ProducingActivityTypeEnum.ProductionManager,
    "Publizist; Publizistin": efi.ProducingActivityTypeEnum.Publicist,
}
