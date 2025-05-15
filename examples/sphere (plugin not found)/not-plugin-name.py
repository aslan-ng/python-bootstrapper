"""
This example tries to override the default area and volume implementation for a sphere.
But, the filename is not recognized as a plugin name. So, the default implementation will be used.
"""
from package import Shape


class MyCustomName(Shape):

    name = "sphere"

    def area(radius):
        return 4 * Shape.pi * radius ** 2
    
    def volume(radius):
        return 4 / 3 * Shape.pi * radius ** 3