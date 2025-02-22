"""
Write a program that prompts the user to input a number and reverse its digits. For
example, the reverse of 12345 is 54321; reverse of 5600 is 65.
"""

num=int(input("Enter the number :~ "))
n= num
rev=0
while n>0:
    a=n%10
    rev= rev*10+a
    n=n//10
print("Reverse order : ",rev)