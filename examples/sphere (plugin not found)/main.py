"""
This example tries to override the default area and volume implementation for a sphere but fails to do so.
"""
from package import Shape


radius = 10
print(Shape.name)  # → "circle"
print(f"Area of {Shape.name} when radius is {radius}: ", Shape.area(radius=10))  # → 314.159
try:
    print(f"Volume of {Shape.name} when radius is {radius}: ", Shape.volume(radius=10))  # → Error
except:
    print("Successfully raied error when asked about the volume.")