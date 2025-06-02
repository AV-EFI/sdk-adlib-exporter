from builder.base.base_builder import BaseBuilder
from builder.base.utils import get_mapped_enum_value
from mappings.work_form_enum_mapping import work_form_enum_mapping


def compute_has_form(record: BaseBuilder):
    nfa_categories = record.xml.get_all("nfa_category/value[@lang='3']/text()")

    if not nfa_categories:
        return None

    work_forms = []

    for category in nfa_categories:
        work_form = get_mapped_enum_value(work_form_enum_mapping, category)

        if work_form is None:
            continue

        work_forms.append(work_form_enum_mapping[category])

    return work_forms
