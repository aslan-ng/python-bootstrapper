"""
This is the main module of the package.
As default, it calculate the area of circle, but volume is not implemented.
"""
from package.constants import Constants
from package.calculations import Calculations


class Shape(Constants, Calculations):
    """
    This is the main class that combines the subclasses Constants, Area, and Volume.
    As default, it calculates the area of a circle, but volume is not implemented.
    """
    pass


if __name__ == "__main__":
    radius = 10
    print(f"Area of {Shape.name} when radius is {radius}: ", Shape.area(radius=10))  # → 314.159
    try:
        print(f"Volume of {Shape.name} when radius is {radius}: ", Shape.volume(radius=10))
    except:
        print("Successfully raied error when asked about the volume.")
