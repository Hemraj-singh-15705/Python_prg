"""
Write a program which accept principle, rate and time from user and print the simple
interest. The formula to calculate simple interest is: simple 
interest = principle x rate x time / 100
"""

pri=int(input("Enter the principle amount : "))
rate= int(input("Enter the rate : "))
time=int(input("Enter the time : "))

si=(pri*rate*time)//100
print("Simple Interest : ~",si)