import os
from adlib.provider import RecordProvider, PointerFileProvider
from adlib.wrapper import Database
from requests_cache import CachedSession


class CachedDatabase(Database):
    def __init__(self, url):
        super().__init__(url)
        self.session = CachedSession(cache_name="adlib_cache")


try:
    adlib_url = os.environ["SDK_ADLIB_URL"]
    adlib = CachedDatabase(adlib_url)
except KeyError:
    raise EnvironmentError("SDK_ADLIB_URL environment variable is not set.")

# Initialize the different providers for Adlib data retrieval
pointer_file_provider = PointerFileProvider(adlib, database="collect.inf")
collect_provider = RecordProvider(adlib, database="collect.inf")
people_provider = RecordProvider(adlib, database="people.inf")
thesau_provider = RecordProvider(adlib, database="thesau.inf")
