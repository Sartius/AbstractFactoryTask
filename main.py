from BoeingFactory import BoeingFactory
from MesserschmitFactory import MesserschmitFactory

def getPlanes(factory):
    product = factory.getSpeed()
    return product

def main():
    americanplanes = getPlanes(BoeingFactory)
    print(americanplanes.speed)
    germanplanes = getPlanes(MesserschmitFactory)
    print(germanplanes.speed)

if __name__ == "__main__":
    main()