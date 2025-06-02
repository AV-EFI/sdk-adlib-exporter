from mappings.work_variant_type_enum_mapping import work_variant_type_enum_mapping
from records.base.utils import get_mapped_enum_value


def compute_type(record):
    work_description_type = record.xml.get_first(
        "work.description_type/value[@lang='3']/text()"
    )

    if work_description_type is None:
        return None

    return get_mapped_enum_value(work_variant_type_enum_mapping, work_description_type)
