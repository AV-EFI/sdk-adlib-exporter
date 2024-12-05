from avefi_schema import model as efi

from builder.base.mappings.adlib_to_avefi_mappings import title_type_enum_mapping


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

        full_title_text = title_text[0]
        ordering_title_text = None

        # if article present build combined title
        if title_article:  # Please check for correct logic
            full_title_text = title_article[0] + " " + title_text[0]
            ordering_title_text = title_text[0] + ", " + title_article[0]

        try:
            titles.append(
                efi.Title(
                    has_name=full_title_text,
                    type=title_type_enum_mapping.get(title_type[0]),
                    has_ordering_name=ordering_title_text,
                )
            )
        except IndexError:
            # When no title provided
            assert len(title_type) == 0
            titles.append(
                efi.Title(
                    has_name=full_title_text,
                    type=efi.TitleTypeEnum.AlternativeTitle,
                    has_ordering_name=ordering_title_text,
                )
            )
        except Exception as e:
            # when type not provided, should we omit?
            raise Exception("Problem with Title:", e)

    def title_sort(title):
        if str(title.type) == str(efi.TitleTypeEnum.PreferredTitle.text):
            return 0
        if str(title.type) == str(efi.TitleTypeEnum.SuppliedDevisedTitle.text):
            return 1
        return 2

    # Please check for correct logic
    titles.sort(key=lambda x: title_sort(x))

    return titles[0], titles[1:]
