from abc import ABC, abstractmethod
from PlaneFactory import PlaneFactory
class BoeingFactory(PlaneFactory):

    @classmethod
    @abstractmethod
    def planeTypes(cls):
        return tuple(["_Thunderbolt","_Mustang"])