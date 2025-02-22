"""
 Two numbers are entered through the keyboard. Write a program to find the value of one number raised to the power of another.
"""

n=int(input("Enter the number :~ "))
m=int(input("Enter the power :~ "))
pow=1
for i in range(1,m+1):
    pow= pow*n
print(pow)