"""
Write a program that asks the user to input his name and print its initials. Assuming
that the user always types first name, middle name and last name and does not include
any unnecessary spaces.


For example, if the user enters Ajay Kumar Garg the program should display A. K. G.
Note:Don't use split() method

"""

s=input("Enter a string :~")
for i in s:
    ch=i
    if i.isupper():
        print(i,".",end="  ")
    