"""
This example demonstrates how to use plugin to customzie previously implemented method.
"""
from package import Shape


side = 10
print(f"Area of {Shape.name} when side is {side}: ", Shape.area(side=side))  # → 600
print(f"Volume of {Shape.name} when side is {side}: ", Shape.volume(side=side))  # → 1000