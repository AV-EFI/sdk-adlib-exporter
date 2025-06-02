from avefi_schema import model as efi

from builder.base.base_builder import BaseBuilder


def compute_has_identifier(record: BaseBuilder):
    identifiers = [efi.LocalResource(id=record.priref)]

    pid = record.xml.get_first("PIDdata/PID_data_URI/text()")
    if pid is not None:
        identifiers.append(efi.AVefiResource(id=pid))

    return identifiers
