from mappings import item_element_type_enum_mapping


def compute_element_type(self):
    element_types = self.xml.xpath(
        "mat_characteristics/mat_characteristics.material_type_film/value[@lang='de-DE']/text()"
    )

    if not element_types:
        # no element types at all
        return None

    if not element_types[0] in item_element_type_enum_mapping:
        raise Exception("No mapping found for key:", element_types[0])

    if item_element_type_enum_mapping[element_types[0]] is None:
        # mapping key covered but no mapping value provided, see item_element_type_enum_mapping
        return None

    return item_element_type_enum_mapping[element_types[0]]
