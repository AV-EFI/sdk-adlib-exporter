from avefi_schema import model as efi

from mappings.unit_enum_mapping import unit_enum_mapping


def compute_has_extent(self):
    dimension_extent = get_dimension_extent(self)

    if dimension_extent:
        return dimension_extent

    total_filesize_extent = get_total_filesize_extent(self)

    if total_filesize_extent:
        return total_filesize_extent

    return


def get_dimension_extent(self):
    dimension_list = self.xml.xpath(
        "Dimension[dimension.type/value[@lang='de-DE' and text()='Länge']]"
    )
    if dimension_list:
        unit_list = dimension_list[0].xpath("dimension.unit/value/text()")
        value_list = dimension_list[0].xpath("dimension.value/text()")

        if not unit_list or not value_list:
            return

        unit = unit_list[0]
        value = value_list[0]

        if unit not in unit_enum_mapping:
            raise Exception("No mapping found for key:", unit)

        if unit_enum_mapping[unit] is None:
            return

        return efi.Extent(
            has_value=value,
            has_precision=efi.PrecisionEnum.Approximate,
            has_unit=unit_enum_mapping[unit],
        )
    return


def get_total_filesize_extent(self):
    total_filesize_list = self.xml.xpath("total_filesize/text()")
    if not total_filesize_list:
        return
    total_filesize = total_filesize_list[0]

    return efi.Extent(
        has_value=total_filesize,
        has_precision=efi.PrecisionEnum.Approximate,
        has_unit=efi.UnitEnum.GigaByte,
    )
