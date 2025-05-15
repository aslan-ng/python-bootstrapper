"""
The main module has implementation of area for circle by default.
But, volume is not defined for circle; therefore, it is not implemented.
Basically, there is nothing to customize in this example.
"""
from package import Shape


radius = 10
print(f"Area of {Shape.name} when radius is {radius}: ", Shape.area(radius=10))  # → 314.159
try:
    print(f"Volume of {Shape.name} when radius is {radius}: ", Shape.volume(radius=10))
except:
    print("Successfully raied error when asked about the volume.")