from mappings import work_form_enum_mapping


def compute_has_form(self):
    nfa_categories = self.xml.xpath("nfa_category/value[@lang='3']/text()")

    # Please check for correct logic
    if not nfa_categories:
        return None

    return [work_form_enum_mapping.get(nfa_category) for nfa_category in nfa_categories]
