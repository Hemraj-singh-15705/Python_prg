"""
A palindromic number is a number that remains the same when its digits are
reversed. For example, 16461. Write a program that prompts the user to input a number
and determine whether the number is palindrome or not.
"""

num=int(input("Enter the number :~ "))
n= num
rev=0
while n>0:
    a=n%10
    rev= rev*10+a
    n=n//10


if rev == num:
    print("Number is Palindromic ")
else:
    print("Not a Palindrome number :")