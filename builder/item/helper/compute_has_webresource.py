from avefi_schema import model as efi

from builder.base.base_builder import BaseBuilder


def compute_has_webresource(record: BaseBuilder):
    uri = (
        "https://sammlungen.deutsche-kinemathek.de/recherche/itemdetails/sdk"
        + record.priref
    )
    return efi.HttpUri(uri)
