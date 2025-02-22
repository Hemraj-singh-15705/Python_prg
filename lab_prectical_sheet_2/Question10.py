"""
Suppose a, b, and c denote the lengths of the sides of a triangle. Then the area of
the triangle can be calculated using the formula:
where
Write a program that asks the user to input the length of sides of the triangle and print
the area.
"""
import math
sideA=int(input("Enter the Side A : ~"))
sideB=int(input("Enter the Side B : ~"))
sideC=int(input("Enter the Side C : ~"))
s=(sideA+sideB+sideC)//2
area=(s*(s-sideA)*(s-sideB)*(s-sideC))
print("Area of ~ ",math.sqrt(area))



# not working right