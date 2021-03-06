#! python3
#
# Find the hypotenuse
# Your program will ask the user to enter in the 2 short sides of a right triangle.
# You will calculate the length of the hypotenuse and display the result.
# You will need to use the math module to use the command that finds the square root.
#
# Inputs:
# side, side
#
# Outputs:
# hypotenuse
#
# Test output
# input sides of 5 and 7 should give hypotenuse of 8.60232526704

from math import sqrt

sidea = input("Please enter the length of 1 side of a triangle:").strip()
sideb = input("Please enter another side length of a triangle:").strip()

sidea = int(sidea)
sideb = int(sideb)

hyp = sqrt(sidea * sidea + sideb * sideb)

print(hyp)
