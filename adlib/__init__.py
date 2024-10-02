import os
from adlib.provider import RecordProvider, PointerFileProvider
from adlib.wrapper import Database

# Attempt to retrieve the Adlib URL from environment variables
try:
    adlib_url = os.environ["SDK_ADLIB_URL"]
    adlib = Database(adlib_url)
except KeyError:
    raise EnvironmentError("SDK_ADLIB_URL environment variable is not set.")

# Initialize the different providers for Adlib data retrieval
pointer_file_provider = PointerFileProvider(
    adlib, cache=True, _dir="pointer", database="collect.inf"
)
collect_provider = RecordProvider(
    adlib, cache=True, _dir="collect", database="collect.inf"
)
people_provider = RecordProvider(
    adlib, cache=True, _dir="people", database="people.inf"
)
thesau_provider = RecordProvider(
    adlib, cache=True, _dir="thesau", database="thesau.inf"
)
