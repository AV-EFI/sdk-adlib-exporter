from avefi_schema import model as efi

publication_event_type_enum = {
    "Fernsehausstrahlung": efi.PublicationEventTypeEnum.BroadcastEvent,
    "Heimkino": efi.PublicationEventTypeEnum.HomeVideoPublicationEvent,
    "Nicht-Kino-Distribution": efi.PublicationEventTypeEnum.NonTheatricalDistributionEvent,
    "Nicht veröffentlicht": efi.PublicationEventTypeEnum.NotForReleaseEvent,
    "Internet": efi.PublicationEventTypeEnum.OnlineTransmissionEvent,
    "Pre-Release": efi.PublicationEventTypeEnum.PreReleaseEvent,
    "Kino-Distribution": efi.PublicationEventTypeEnum.TheatricalDistributionEvent,
    "Unbekannt": efi.PublicationEventTypeEnum.UnknownEvent,
    # Covered keys without mapping! Please provide mapping! #
    "Restauriert": None,
    "Ohne Distribution (Privatfilme)": None,
    "Nicht zugeordnet (Altdaten)": None,
    "Aufführung (Verbreitungsgebiet unbekannt)": None,
    "Uraufführung": None,
}
