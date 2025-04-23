from abc import ABC, abstractmethod


class BaseBuilder(ABC):
    def __init__(self, xml, allowed_parents, priref):
        self.xml = xml
        self.allowed_parents = allowed_parents
        self.priref = priref

    @abstractmethod
    def build(self):
        pass
