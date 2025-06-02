from builder.base.base_builder import BaseBuilder
from mappings.work_form_enum_mapping import work_form_enum_mapping


def compute_has_form(record: BaseBuilder):
    nfa_categories = record.xml.get_all("nfa_category/value[@lang='3']/text()")

    if not nfa_categories:
        return None

    work_forms = []

    for category in nfa_categories:
        if category not in work_form_enum_mapping:
            raise Exception("No mapping found for key:", category)

        if work_form_enum_mapping[category] is None:
            continue

        work_forms.append(work_form_enum_mapping[category])

    return work_forms
