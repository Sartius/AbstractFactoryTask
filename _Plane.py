from abc import ABC,abstractmethod

class _Plane(ABC):
    def __init__(self, factoryName=None):
        self.type = "fighter"
        self.manufactured = factoryName

    @property
    @abstractmethod
    def speed(self):
        pass