from avefi_schema import model as efi

from records.base.base_record import XMLAccessor


def compute_has_identifier(xml: XMLAccessor):
    identifiers = [efi.LocalResource(id=xml.xpath("@priref")[0])]

    pid_url = xml.get_first("PIDdata/PID_data_URI/text()")

    if pid_url is not None:
        pid = pid_url.split("https://hdl.handle.net/")[-1]

        identifiers.append(efi.AVefiResource(id=pid))

    return identifiers
