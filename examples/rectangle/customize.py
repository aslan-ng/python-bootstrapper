"""
This example overrides the default area implementation for a rectangle.
Volume is not defined for rectangles, so it is not overridden.
"""
from package import Math


class MyCustomPlugin(Math):

    def area(width, height):
        return width * height