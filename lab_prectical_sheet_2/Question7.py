"""
Write a program that prompts the user to enter number in two variables and swap
the contents of the variables.(Do not declare extra variable.)
"""

num1=int(input("Enter the num1 : "))
num2=int(input("Enter the num2 : "))
num1,num2 = num2,num1
print("After the Swap ")
print("Num1 =",num1)
print("Num2 =",num2)