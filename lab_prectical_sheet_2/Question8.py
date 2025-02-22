"""
Write a program that prompts the user to input the radius of a circle and outputs the
area and circumference of the circle. The formula is
Area = pi x radius2
Circumference = 2 x pi x radius
"""


radius=int(input("Enter the radius : ~ "))
pi=3.14
print("Area : ~ ",pi*(radius**2))
print("Circumference = ",2*pi*radius)