from avefi_schema import model as efi

from records.record import XMLAccessor


def has_webresource(xml: XMLAccessor):
    uri = (
        "https://sammlungen.deutsche-kinemathek.de/recherche/itemdetails/sdk"
        + xml.xpath("@priref")[0]
    )
    return efi.HttpUri(uri)
