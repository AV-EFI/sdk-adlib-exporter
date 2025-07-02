from records.base.belongs_to import belongs_to
from records.record import XMLAccessor


def is_item_of(xml: XMLAccessor):
    return belongs_to(xml)[0]
