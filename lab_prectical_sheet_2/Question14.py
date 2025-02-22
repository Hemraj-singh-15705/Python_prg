"""
Write a program that prompts the user to input three integers and outputs the largest.
"""

first=int(input("Enter the first number ~"))
second=int(input("Enter the Second number ~"))
third=int(input("Enter the third number ~"))
if first > second and first > third:
    print("largest number is ",first)
elif second > first and second > third:
    print("largest number is ",second)
else:
    print("largest number is ",third)