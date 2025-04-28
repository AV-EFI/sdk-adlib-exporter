from mappings.item_element_type_enum_mapping import item_element_type_enum_mapping


def compute_element_type(self):
    element_types = self.xml.xpath(
        "mat_characteristics/mat_characteristics.material_type_film/value[@lang='de-DE']/text()"
    )

    if not element_types:
        return None

    if element_types[0] not in item_element_type_enum_mapping:
        raise Exception("No mapping found for key:", element_types[0])

    if item_element_type_enum_mapping[element_types[0]] is None:
        return None

    return item_element_type_enum_mapping[element_types[0]]
