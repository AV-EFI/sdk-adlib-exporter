from mappings.work_variant_type_enum_mapping import work_variant_type_enum_mapping


def compute_type(self):
    worklevel_type = self.xml.xpath("work.description_type/value[@lang='3']/text()")[0]

    if worklevel_type not in work_variant_type_enum_mapping:
        raise Exception("No mapping found for key:", worklevel_type)

    return work_variant_type_enum_mapping.get(worklevel_type)
