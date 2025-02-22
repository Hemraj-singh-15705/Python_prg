"""
Write a program that prompts the user to input the length and the width of a
rectangle and outputs the area and circumference of the rectangle. The formula is
Area = Length x Width
Circumference = 2 x ( Length + Width)
"""

Length = int(input("Enter the Length : "))
Width = int(input("Enter the Width : "))
Area = Length*Width
Circumference = 2*( Length + Width)
print("Area ~ ",Area)
print("Circumference ~ ",Circumference)