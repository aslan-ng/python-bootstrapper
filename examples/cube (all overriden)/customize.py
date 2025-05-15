"""
This example overrides the default area and volume implementation for a cube.
"""
from package import Shape


class MyCustomPlugin(Shape):

    name = "cube"

    def area(side):
        return 6 * side ** 2

    def volume(side):
        return side ** 3