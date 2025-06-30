from avefi_schema import model as efi

from records.base.base_record import XMLAccessor


def compute_has_webresource(xml: XMLAccessor):
    uri = (
        "https://sammlungen.deutsche-kinemathek.de/recherche/itemdetails/sdk"
        + xml.xpath("@priref")[0]
    )
    return efi.HttpUri(uri)
