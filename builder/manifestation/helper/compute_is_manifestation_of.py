from builder.base.helper.compute_belong_to import compute_belongs_to


def compute_is_manifestation_of(self):
    return compute_belongs_to(self)
