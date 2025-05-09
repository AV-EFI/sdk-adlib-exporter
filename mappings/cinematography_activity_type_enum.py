from avefi_schema import model as efi

cinematography_activity_type_enum = {
    "Kameraassistenz": efi.CinematographyActivityTypeEnum.CameraAssistant,
    "Kameraoperateur/in": efi.CinematographyActivityTypeEnum.CameraOperator,
    "Kamera": efi.CinematographyActivityTypeEnum.Cinematographer,
    "Elektrik": efi.CinematographyActivityTypeEnum.Electrician,
    "Oberbeleuchter/in": efi.CinematographyActivityTypeEnum.GafferLighting,
    "Kamerabühne": efi.CinematographyActivityTypeEnum.Grip,
    "2. Kameraassistenz": efi.CinematographyActivityTypeEnum.LoaderClapper,
    "2nd Unit Kamera": efi.CinematographyActivityTypeEnum.SecondUnitDirectorofPhotography,
    "Steadicam-Operateur/in": efi.CinematographyActivityTypeEnum.SteadicamOperator,
    "Standfotos (Credit)": efi.CinematographyActivityTypeEnum.StillPhotographer,
}
