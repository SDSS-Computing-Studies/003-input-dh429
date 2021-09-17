#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.09733552923254

import math

radius = input("Enter the radius of a sphere. ")

radius = int(radius)

volume = 4/3 * 3.141592653589793 * radius ** 3

print(volume)