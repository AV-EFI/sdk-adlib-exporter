from avefi_schema import model as efi

from mappings.unit_enum import unit_enum
from records.base.base_record import BaseRecord
from records.base.utils import get_mapped_enum_value


def compute_has_extent(record: BaseRecord):
    dimension_extent = get_dimension_extent(record)

    if dimension_extent:
        return dimension_extent

    total_filesize_extent = get_total_filesize_extent(record)

    if total_filesize_extent:
        return total_filesize_extent

    return None


def get_dimension_extent(record: BaseRecord):
    unit = record.xml.get_first(
        "Dimension[dimension.type/value[@lang='de-DE' and text()='Länge']]/dimension.unit/value/text()"
    )
    value = record.xml.get_first(
        "Dimension[dimension.type/value[@lang='de-DE' and text()='Länge']]/dimension.value/text()"
    )

    if unit is None or value is None:
        return None

    unit_mapped = get_mapped_enum_value(unit_enum, unit)

    if unit_mapped is None:
        return None

    return efi.Extent(
        has_value=value,
        has_precision=efi.PrecisionEnum.Approximate,
        has_unit=unit_mapped,
    )


def get_total_filesize_extent(record: BaseRecord):
    total_filesize = record.xml.get_first("total_filesize/text()")

    if total_filesize is None:
        return None

    return efi.Extent(
        has_value=total_filesize,
        has_precision=efi.PrecisionEnum.Approximate,
        has_unit=efi.UnitEnum.GigaByte,
    )
