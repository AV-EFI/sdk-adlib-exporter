from avefi_schema import model as efi
from mappings import precision_enum_mapping


def compute_has_duration(self):
    dimensions = self.xml.xpath(
        "Dimension[dimension.type/value[@lang='de-DE' and text()='Laufzeit']]"
    )

    if not dimensions:
        return None

    # I found two occurences of more than one laufzeit dimension 150238552, 150234901
    dimension_xml = dimensions[0]

    value_xml = dimension_xml.xpath("dimension.value/text()")
    if not value_xml:
        # No value in Dimension object
        return None

    value = value_xml[0]

    precision_xml = dimension_xml.xpath("dimension.precision/value[@lang='3']/text()")
    precision = precision_xml[0] if precision_xml else None

    if precision is not None and precision not in precision_enum_mapping:
        raise Exception("No mapping found for key:", precision)

    return efi.Duration(
        has_value=time_string_to_iso_8601_duration(value),
        has_precision=precision_enum_mapping.get(precision),
    )


def time_string_to_iso_8601_duration(time_str):

    minute_str, second_str = time_str.split(".") if "." in time_str else (time_str, "0")

    minutes = int(minute_str)
    seconds = int(second_str)

    hours = minutes // 60
    minutes = minutes % 60

    iso_period = "PT"

    if hours > 0:
        iso_period += f"{hours}H"
    if minutes > 0 or seconds > 0:
        iso_period += f"{minutes}M"
    if seconds > 0:
        iso_period += f"{seconds}S"

    return iso_period
