import inspect
from builder.work.helper.compute_has_event import compute_has_event
from builder.work.helper.compute_has_form import compute_has_form
from builder.work.helper.compute_has_genre import compute_has_genre
from builder.work.helper.compute_has_subject import compute_has_subject
from builder.work.helper.compute_is_part_of import compute_is_part_of
from builder.work.helper.compute_same_as import compute_same_as
from builder.work.helper.compute_type import compute_type
from builder.work.helper.compute_title import (
    compute_has_primary_title,
    compute_has_alternative_title,
)


__all__ = [
    name for name, obj in globals().items() if callable(obj) and inspect.isfunction(obj)
]
