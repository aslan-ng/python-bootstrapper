"""
This example tries to override the default area and volume implementation for a sphere but fails to do so.
"""
from package import Math


radius = 10
print("pi: ", Math.pi)  # → 3.14159
print(f"Area of sphere when radius is {radius}: ", Math.area(radius=10))  # → 314.159
try:
    print(f"Volume of sphere when radius is {radius}: ", Math.volume(radius=10))  # → Error
except:
    print("Successfully raied error when asked about the volume.")