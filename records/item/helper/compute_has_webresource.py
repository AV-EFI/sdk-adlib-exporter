from avefi_schema import model as efi

from records.base.base_record import BaseRecord


def compute_has_webresource(record: BaseRecord):
    uri = (
        "https://sammlungen.deutsche-kinemathek.de/recherche/itemdetails/sdk"
        + record.priref
    )
    return efi.HttpUri(uri)
