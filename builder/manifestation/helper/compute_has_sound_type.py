from mappings import sound_type_enum_mapping


def compute_has_sound_type(self):
    sound_list = self.xml.xpath("sound_manifestation/value[@lang='3']/text()")

    if not sound_list:
        return None

    sound = sound_list[0]

    if sound not in sound_type_enum_mapping:
        raise Exception("No mapping found for key:", sound)

    return sound_type_enum_mapping[sound]
