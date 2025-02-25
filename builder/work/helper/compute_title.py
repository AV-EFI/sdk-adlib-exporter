# note alternative title selection for works without titles or missing mapping

from avefi_schema import model as efi
from mappings import title_type_enum_mapping


def compute_has_alternative_title(self):
    _, alternative_titles = compute_title(self)
    return alternative_titles


def compute_has_primary_title(self):
    primary_title, _ = compute_title(self)
    return primary_title


def compute_title(self):

    xml_titles = self.xml.xpath("Title")
    titles = []

    for xml_title in xml_titles:
        title_text = xml_title.xpath("title/text()")
        title_type = xml_title.xpath("title.type/value[@lang='de-DE']/text()")
        title_article = xml_title.xpath("title.article/text()")

        if not title_text:
            continue

        full_title_text = title_text[0]
        ordering_title_text = None

        # if article present build combined title
        if title_article:
            full_title_text = title_article[0] + " " + title_text[0]
            ordering_title_text = title_text[0] + ", " + title_article[0]

        if not title_type:
            titles.append(
                efi.Title(
                    has_name=full_title_text,
                    type=efi.TitleTypeEnum.AlternativeTitle,
                    has_ordering_name=ordering_title_text,
                )
            )
            continue

        if title_type[0] not in title_type_enum_mapping:
            raise Exception("No mapping found for key:", title_type[0])

        if title_type_enum_mapping[title_type[0]] is None:
            titles.append(
                efi.Title(
                    has_name=full_title_text,
                    type=efi.TitleTypeEnum.AlternativeTitle,
                    has_ordering_name=ordering_title_text,
                )
            )
            continue

        titles.append(
            efi.Title(
                has_name=full_title_text,
                type=title_type_enum_mapping.get(title_type[0]),
                has_ordering_name=ordering_title_text,
            )
        )

    def title_sort(title):
        if str(title.type) == str(efi.TitleTypeEnum.PreferredTitle.text):
            return 0
        if str(title.type) == str(efi.TitleTypeEnum.SuppliedDevisedTitle.text):
            return 1
        return 2

    titles.sort(key=lambda x: title_sort(x))

    return titles[0], titles[1:]
