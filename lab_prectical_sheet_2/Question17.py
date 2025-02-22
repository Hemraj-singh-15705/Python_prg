"""
Write a program that prompts the user to input the value of a (the coefficient of x2), b 
(the coefficient of x), and c (the constant term) and outputs the roots of the quadratic equation
"""

# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = [(b**2) - (4*a*c)]**1//2
# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))