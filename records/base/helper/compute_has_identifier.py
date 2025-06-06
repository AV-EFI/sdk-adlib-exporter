from avefi_schema import model as efi

from records.base.base_record import BaseRecord


def compute_has_identifier(record: BaseRecord):
    identifiers = [efi.LocalResource(id=record.priref)]

    pid_url = record.xml.get_first("PIDdata/PID_data_URI/text()")

    if pid_url is not None:
        pid = pid_url.split("https://hdl.handle.net/")[-1]

        identifiers.append(efi.AVefiResource(id=pid))

    return identifiers
