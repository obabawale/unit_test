# Write a function to calculate the area of a circle
from math import pi

# Area = pi * r ** 2
def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number.")
    if r < 0:
        raise ValueError("The radius cannot be less than zero.")
    return pi * (r**2)
