from mappings.colour_type_enum_mapping import colour_type_enum_mapping


def compute_has_colour_type(self):
    colour_list = self.xml.xpath("colour_manifestation/value[@lang='3']/text()")

    if not colour_list:
        return None

    colour = colour_list[0]

    if colour not in colour_type_enum_mapping:
        raise Exception("No mapping found for key:", colour)

    return colour_type_enum_mapping[colour]
