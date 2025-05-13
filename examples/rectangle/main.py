"""
This example demonstrates how to use plugin to customzie previously implemented method.
"""
from package import Math


width = 10
height = 5
print(f"Area of square when width is {width} and height is {height}: ", Math.area(width=width, height=height))  # → 600
try:
    print(f"Volume of square when width is {width} and height is {height}: ", Math.volume(width=width, height=height))  # → Error
except:
    print("Successfully raied error when asked about the volume.")
