from abc import ABC, abstractmethod
from PlaneFactory import PlaneFactory
class MesserschmitFactory(PlaneFactory):

    @classmethod
    @abstractmethod
    def planeTypes(cls):
        return tuple(["_Bf109","_Me262"])