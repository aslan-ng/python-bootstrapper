"""
This example overrides the default area and volume implementation for a sphere.
"""
from package import Math


class MyCustomName(Math):

    def area(radius):
        return 4 * Math.pi * radius ** 2
    
    def volume(radius):
        return 4 / 3 * Math.pi * radius ** 3