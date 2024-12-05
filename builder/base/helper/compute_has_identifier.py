from avefi_schema import model as efi


def compute_has_identifier(self):
    priref = self.xml.xpath("priref/text()")[0]
    return efi.LocalResource(id=priref)
