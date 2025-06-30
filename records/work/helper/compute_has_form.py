from mappings.work_form_enum import work_form_enum
from records.base.base_record import XMLAccessor
from records.base.utils import get_mapped_enum_value


def compute_has_form(xml: XMLAccessor):
    nfa_categories = xml.get_all("nfa_category/value[@lang='3']/text()")

    if not nfa_categories:
        return None

    work_forms = []

    for category in nfa_categories:
        work_form = get_mapped_enum_value(work_form_enum, category)

        if work_form is None:
            continue

        work_forms.append(work_form_enum[category])

    return work_forms
