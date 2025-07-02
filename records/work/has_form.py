from mappings.loader import get_mapping
from records.record import XMLAccessor
from records.utils import get_mapped_enum_value


def has_form(xml: XMLAccessor):
    nfa_categories = xml.get_all("nfa_category/value[@lang='3']/text()")

    if not nfa_categories:
        return None

    work_forms = []

    for category in nfa_categories:
        work_form = get_mapped_enum_value("WorkFormEnum", category)

        if work_form is None:
            continue

        work_forms.append(get_mapping("WorkFormEnum")[category])

    return work_forms
