from avefi_schema import model as efi


def compute_has_item(self):
    parts_list = self.xml.xpath("Parts/parts.recordnumber/text()")

    return [efi.LocalResource(id=priref) for priref in parts_list]
