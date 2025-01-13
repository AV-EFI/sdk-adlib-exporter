from abc import abstractmethod, ABC


class BaseProvider(ABC):
    def __init__(self, adlib, database):
        self.adlib = adlib
        self.database = database

    def get_by_priref(self, priref):
        query = self._construct_query(priref)
        data_xml = self._execute_query(query)

        return data_xml

    def _execute_query(self, query):
        try:
            return self.adlib.get(query).records[0]
        except Exception as e:
            print(f"An error occurred during the request: {e}")
            return None

    @abstractmethod
    def _construct_query(self, priref):
        pass


class RecordProvider(BaseProvider):
    def _construct_query(self, priref):

        return {
            "search": f"priref={priref}",
            "database": self.database,
            "xmltype": "grouped",
        }


class PointerFileProvider(BaseProvider):
    def _construct_query(self, priref):

        return {
            "database": self.database,
            "xmltype": "grouped",
            "command": "getpointerfile",
            "number": priref,
        }
