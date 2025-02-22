"""
Write a program that prompts the user to input a number and prints its factorial. The
factorial of an integer n is defined as n! = 1 x 2 x 3 x ... x n; if n > 0 = 1; if n = 0 For
instance, 6! can be calculated as 1 x 2 x 3 x 4 x 5 x 6
"""

n=int(input("Enter the number : ~ "))
fact=1
for i in range(1,n+1,1):
    fact *=i 
print("Factorial is : ",fact)