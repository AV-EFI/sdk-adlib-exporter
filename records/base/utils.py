import re

from avefi_schema import model as efi


def get_formatted_date(date_start, date_start_prec, date_end, date_end_prec):
    production_date_start_value = date_start + ("~" if date_start_prec else "")
    production_date_end_value = date_end + ("~" if date_end_prec else "")
    return (
        production_date_start_value
        if production_date_start_value == production_date_end_value
        else f"{production_date_start_value}/{production_date_end_value}"
    )


def get_same_as_for_priref(
    priref,
    provider,
    include_gnd=False,
    include_filmportal=False,
    include_tgn=False,
):

    try:
        same_as = []

        xml_data = provider.get_by_priref(priref)
        xml_sources = xml_data.xpath("Source")

        for source_xml in xml_sources:

            source_number = source_xml.xpath("string(source.number[1])") or None

            if source_number is None:
                continue

            if include_gnd and "d-nb.info/gnd/" in source_number:
                same_as.append(
                    efi.GNDResource(
                        id=source_number.split("/")[-1],
                    )
                )

            if include_filmportal and "www.filmportal.de" in source_number:

                # temporary solution
                filmportal_id = source_number.split("_")[-1]
                if not re.fullmatch(r"^[\da-f]{32}$", filmportal_id):
                    continue

                same_as.append(
                    efi.FilmportalResource(
                        id=filmportal_id,
                    )
                )

            if include_tgn and "vocab.getty.edu/page/tgn/" in source_number:
                same_as.append(
                    efi.TGNResource(
                        id=source_number.split("/")[-1],
                    )
                )
        return same_as

    except Exception as e:
        raise Exception("Problem with same_as computation:", e)


def get_mapped_enum_value(enum_map, key, name=None):
    if key not in enum_map:
        raise Exception(
            f"No mapping found for key: '{key}'{f' in {name}' if name else ''}"
        )

    return enum_map[key]
