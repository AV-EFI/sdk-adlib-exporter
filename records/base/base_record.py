from abc import ABC, abstractmethod


class BaseRecord(ABC):
    def __init__(self, xml, priref):
        self.xml: XMLAccessor = XMLAccessor(xml)
        self.priref = priref

    @abstractmethod
    def build(self):
        pass


class XMLAccessor:
    def __init__(self, xml_element):
        self._element = xml_element

    def get_first(self, xpath_expression):
        elements = self._element.xpath(xpath_expression)

        return elements[0] if elements else None

    def get_all(self, xpath_expression):
        elements = self._element.xpath(xpath_expression)

        if xpath_expression.endswith("/text()"):
            return elements

        return [XMLAccessor(el) for el in elements]

    def __getattr__(self, name):
        return getattr(self._element, name)

    def __repr__(self):
        return f"<XMLAccessor wrapping {self._element!r}>"
