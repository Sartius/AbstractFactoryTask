from abc import ABC, abstractmethod
import random
from _Thunderbolt import _Thunderbolt
from _Mustang import _Mustang
from _Bf109 import _Bf109
from _Me262 import _Me262

class PlaneFactory(ABC):

    @classmethod
    @abstractmethod
    def planeTypes(cls):
        pass

    @classmethod
    @abstractmethod
    def getSpeed(cls):
        randProduct = random.choice(cls.planeTypes())
        # print(randProduct)
        thisModule = __import__(__name__)
        planeClass = getattr(thisModule,randProduct)
        # print(cls.__name__)
        # print(planeClass)
        plane = planeClass(factoryName=cls.__name__)
        return plane
    