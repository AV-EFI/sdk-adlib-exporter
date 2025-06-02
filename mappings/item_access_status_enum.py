from avefi_schema import model as efi

item_access_status_enum = {
    "Archivkopie": efi.ItemAccessStatusEnum.Archive,
    "Verleihkopie": efi.ItemAccessStatusEnum.Distribution,
    "Master": efi.ItemAccessStatusEnum.Master,
    "Removed": efi.ItemAccessStatusEnum.Removed,
    "Viewing": efi.ItemAccessStatusEnum.Viewing,
    # Covered keys without mapping! Please provide mapping! #
    "Kassation": None,
    "Mastermaterial": None,
    "Sichtungskopie": None,
    "Verschollen": None,
    "Tausch/Abgabe": None,
}
