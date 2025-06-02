from abc import ABC, abstractmethod


class BaseBuilder(ABC):
    def __init__(self, xml, allowed_parents, priref):
        self.xml: XMLContainer = XMLContainer(xml)
        self.allowed_parents = allowed_parents
        self.priref = priref

    @abstractmethod
    def build(self):
        pass


class XMLContainer:
    def __init__(self, xml):
        self.xml = xml

    def get_first(self, xpath_expression):
        results = self.xml.xpath(xpath_expression)

        return results[0] if results else None

    def get_all(self, xpath_expression):
        return self.xml.xpath(xpath_expression)
