from avefi_schema import model as efi
from adlib import thesau_provider


def compute_has_genre(self):
    xml_content_genres = self.xml.xpath("Content_genre")

    genres = []

    try:
        for xml_content_genre in xml_content_genres:
            genre_name_list = xml_content_genre.xpath("content.genre/value/text()")
            priref_list = xml_content_genre.xpath("content.genre.lref/text()")
            if not genre_name_list or not priref_list:
                # sometimes a genre is provided but the not name or priref e.g. 150007840.xml
                continue
            genre_name = genre_name_list[0]
            priref = priref_list[0]
            # print(genre_name, priref)
            genre_xml = thesau_provider.get_by_priref(priref)
            sources_xml = genre_xml.xpath("Source")

            same_as = []

            for source_xml in sources_xml:
                term_number_list = source_xml.xpath("term.number/text()")
                if not term_number_list:
                    # sometimes a source is provided but the term_number field is just empty e.g. 8072.xml
                    continue
                term_number = term_number_list[0]
                if "http://d-nb.info/gnd/" in term_number:
                    same_as.append(
                        efi.GNDResource(
                            id=term_number.split("/")[-1],
                        )
                    )

            genre = efi.Genre(has_name=genre_name, same_as=same_as)
            genres.append(genre)

    except Exception as e:
        # when type not provided
        raise Exception("Problem with Content_Genre:", e)

    return genres
