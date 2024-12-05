from avefi_schema import model as efi


def compute_has_webresource(self):
    uri = (
        "https://sammlungen.deutsche-kinemathek.de/recherche/itemdetails/sdk"
        + self.xml.xpath("priref/text()")[0]
    )
    return efi.HttpUri(uri)
