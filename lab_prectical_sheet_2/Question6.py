"""
Write a program that prompts the user to enter number in two variables and swap
the contents of the variables
"""

num1=int(input("Enter the num1 : "))
num2=int(input("Enter the num2 : "))
temp=num1
num1=num2
num2=temp
print("After the Swap ")
print("Num1 =",num1)
print("Num2 =",num2)