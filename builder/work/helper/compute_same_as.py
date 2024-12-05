from avefi_schema import model as efi


def compute_same_as(self):
    # currently only generating "avefi:FilmportalResource"
    xml_alternative_numbers = self.xml.xpath("Alternative_number")

    try:
        for xml_alternative_number in xml_alternative_numbers:
            number_list = xml_alternative_number.xpath("alternative_number/text()")
            number_type_list = xml_alternative_number.xpath(
                "alternative_number.type/value/text()"
            )
            if not number_type_list or not number_list:
                # skip when not both are provided e.g. 150000691.xml
                continue
            number_type = number_type_list[0]
            number = number_list[0]

            if number_type == "ref_filmportal":
                return efi.FilmportalResource(id=number)
    except Exception as e:
        # when type not provided
        raise Exception("Problem with Alternative_number:", e)

    return None
