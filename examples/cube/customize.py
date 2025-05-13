"""
This example overrides the default area and volume implementation for a cube.
"""
from package import Math


class MyCustomPlugin(Math):

    def area(side):
        return 6 * side ** 2

    def volume(side):
        return side ** 3