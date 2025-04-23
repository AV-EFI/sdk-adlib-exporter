from avefi_schema import model as efi


def compute_has_identifier(self):
    identifiers = []

    priref = self.xml.xpath("priref/text()")[0]
    identifiers.append(efi.LocalResource(id=priref))

    pid_list = self.xml.xpath("PIDdata/PID_data_URI/text()")
    if pid_list is not None and len(pid_list) == 1:
        identifiers.append(efi.AVefiResource(id=pid_list[0]))

    return identifiers
