"""
This is the main module of the package.
As default, it calculate the area of circle, but volume is not implemented.
"""
from package.constants import Constants
from package.area import Area
from package.volume import Volume


class Math(Constants, Area, Volume):
    """
    This is the main class that combines the subclasses Constants, Area, and Volume.
    As default, it calculates the area of a circle, but volume is not implemented.
    """
    pass


if __name__ == "__main__":
    radius = 10
    print("pi: ", Math.pi)
    print(f"Area of circle when radius is {radius}: ", Math.area(radius=10))
    try:
        print(f"Volume of circle when radius is {radius}: ", Math.volume(radius=10))
    except:
        print("Successfully raied error when asked about the volume.")
