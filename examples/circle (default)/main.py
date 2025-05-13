"""
The main module has implementation of area for circle by default.
But, volume is not defined for circle; therefore, it is not implemented.
Basically, there is nothing to customize in this example.
"""
from package import Math


radius = 10
print("pi: ", Math.pi)  # → 3.14159
print(f"Area of circle when radius is {radius}: ", Math.area(radius=10))  # → 314.159
try:
    print(f"Volume of circle when radius is {radius}: ", Math.volume(radius=10))
except:
    print("Successfully raied error when asked about the volume.")