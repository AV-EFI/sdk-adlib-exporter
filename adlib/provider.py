import os
import shutil
from abc import abstractmethod, ABC
from lxml import etree


class BaseProvider(ABC):
    """
    Base class for Adlib data providers with optional caching mechanism for XML files.

    Attributes:
        adlib: The Adlib database connection.
        cache: Boolean indicating whether caching is enabled.
        _dir: Directory path where cached files are stored.
        database: Name of the database to query.
    """

    def __init__(self, adlib, cache, _dir, database):
        """
        Initializes the BaseProvider with caching options and prepares the directory for cache storage.

        Args:
            adlib: The Adlib connection object for querying the database.
            cache: A boolean flag indicating whether to enable caching.
            _dir: Directory path to store cached XML files.
            database: The name of the database to query.
        """
        self.cache = cache
        self.adlib = adlib
        self._dir = _dir
        self.database = database

        # Create cache directory if it doesn't exist
        if not os.path.isdir(_dir):
            os.mkdir(_dir)

        # If caching is disabled, clear existing cached files
        if not cache:
            shutil.rmtree(_dir)
            os.mkdir(_dir)

    def get_by_priref(self, priref):
        """
        Retrieves the XML data for a given priref. If caching is enabled and the data is available,
        it retrieves it from the cache; otherwise, it queries the database and stores the result in cache.

        Args:
            priref: The priref (primary reference number) for which to fetch the XML data.

        Returns:
            The XML data as an `Element` object.
        """
        file_path = os.path.join(self._dir, f"{priref}.xml")

        # Load from cache if available and caching is enabled
        if self.cache and os.path.isfile(file_path):
            return self.__load_from_cache(file_path)

        # Construct the query and fetch the data from the database
        query = self._construct_query(priref)
        data_xml = self.__execute_query(query)

        # Save the result in cache if data is fetched successfully
        if data_xml is not None:
            self.__save_to_cache(data_xml, file_path)

        return data_xml

    @staticmethod
    def __load_from_cache(file_path):
        """
        Loads XML data from the cache.

        Args:
            file_path: The path to the cached XML file.

        Returns:
            The root of the parsed XML tree.

        Raises:
            Exception: If there is an XML parsing error.
        """
        with open(file_path, "rb") as file:
            try:
                tree = etree.parse(file)
                return tree.getroot()
            except etree.XMLSyntaxError as e:
                raise Exception(f"Failed to parse {file_path}: {e}")

    @staticmethod
    def __save_to_cache(data_xml, file_path):
        """
        Saves XML data to the cache.

        Args:
            data_xml: The XML data to be saved.
            file_path: The path where the XML data should be saved.

        Raises:
            Exception: If an error occurs while saving the XML data.
        """
        try:
            et = etree.ElementTree(data_xml)
            et.write(file_path, pretty_print=True)
        except Exception as e:
            raise Exception(f"Failed to save {file_path}: {e}")

    def __execute_query(self, query):
        """
        Executes a database query and returns the first record.

        Args:
            query: The query dictionary to be sent to the Adlib database.

        Returns:
            The first record from the query response, or None if the query fails.

        Raises:
            Exception: If an error occurs during the database query.
        """
        try:
            return self.adlib.get(query).records[0]
        except Exception as e:
            print(f"An error occurred during the request: {e}")
            return None

    @abstractmethod
    def _construct_query(self, priref):
        """
        Constructs the specific query for fetching data from the database.

        Args:
            priref: The priref for which to build the query.

        Returns:
            A dictionary representing the database query.

        Note:
            This method must be implemented by child classes.
        """


class RecordProvider(BaseProvider):
    """
    A provider class for retrieving individual records from the Adlib database based on priref.
    """

    def _construct_query(self, priref):
        """
        Constructs a query to retrieve a specific record by priref.

        Args:
            priref: The priref of the record.

        Returns:
            A dictionary representing the query for retrieving a record.
        """
        return {
            "search": f"priref={priref}",
            "database": self.database,
            "xmltype": "grouped",
        }


class PointerFileProvider(BaseProvider):
    """
    A provider class for retrieving pointer files from the Adlib database using the getpointerfile command.
    """

    def _construct_query(self, priref):
        """
        Constructs a query to retrieve a pointer file by priref.

        Args:
            priref: The priref of the pointer file.

        Returns:
            A dictionary representing the query for retrieving a pointer file.
        """
        return {
            "database": self.database,
            "xmltype": "grouped",
            "command": "getpointerfile",
            "number": priref,
        }
