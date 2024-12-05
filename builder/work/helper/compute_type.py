from builder.base.mappings.adlib_to_avefi_mappings import work_variant_type_enum_mapping


def compute_type(self):
    worklevel_type = self.xml.xpath("worklevel_type/value[@lang='3']/text()")[0]

    return work_variant_type_enum_mapping.get(worklevel_type)
