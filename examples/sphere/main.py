"""
This example overrides the default area and volume implementation for a sphere.
"""
from package import Math


radius = 10
print("pi: ", Math.pi)  # → 3.14159
print(f"Area of sphere when radius is {radius}: ", Math.area(radius=10))  # → 1256.636
print(f"Volume of sphere when radius is {radius}: ", Math.volume(radius=10))  # → 4188.787