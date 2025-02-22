"""
Write a program that prompts the user to input a year and determine whether the year is a leap year or not.
"""

year = int(input("Enter the year :~ "))
if year%4==0:
    print(year," is leap year")
else:
    print(year, "is not leap year")