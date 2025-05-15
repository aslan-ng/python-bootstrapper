"""
This example demonstrates how to use plugin to customzie previously implemented method.
"""
from package import Shape


width = 10
height = 5
print(f"Area of {Shape.name} when width is {width} and height is {height}: ", Shape.area(width=width, height=height))  # → 600
try:
    print(f"Volume of {Shape.name} when width is {width} and height is {height}: ", Shape.volume(width=width, height=height))  # → Error
except:
    print("Successfully raied error when asked about the volume.")
