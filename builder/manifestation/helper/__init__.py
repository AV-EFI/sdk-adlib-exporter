import inspect
from builder.manifestation.helper.compute_has_primary_title import (
    compute_has_primary_title,
)
from builder.manifestation.helper.compute_is_manifestation_of import (
    compute_is_manifestation_of,
)
from builder.manifestation.helper.compute_has_duration import compute_has_duration
from builder.manifestation.helper.compute_has_colour_type import compute_has_colour_type
from builder.manifestation.helper.compute_has_sound_type import compute_has_sound_type
from builder.manifestation.helper.compute_has_note import compute_has_note

__all__ = [
    name for name, obj in globals().items() if callable(obj) and inspect.isfunction(obj)
]
