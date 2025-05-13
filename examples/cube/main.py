"""
This example demonstrates how to use plugin to customzie previously implemented method.
"""
from package import Math


side = 10
print(f"Area of square when side is {side}: ", Math.area(side=side))  # → 600
print(f"Volume of square when side is {side}: ", Math.volume(side=side))  # → 1000