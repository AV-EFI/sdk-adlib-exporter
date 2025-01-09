from builder.base.helper.compute_belongs_to import compute_belongs_to


def compute_is_item_of(self):
    return compute_belongs_to(self)[0]
