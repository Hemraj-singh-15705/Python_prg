"""
Write a program in python that accepts a string to setup a passwords. 
Your entered password must meet the following requirements:
 The password must be at least eight characters long.
 It must contain at least one uppercase letter.
 It must contain at least one lowercase letter.
 It must contain at least one numeric digit.
Your program should should perform this validation.
"""

def upper(s):
    for i in s:
        if i.isupper():
            return True

def lower(s):
    for i in s:
        if i.islower():
            return True
        
def digit(s):
    for i in s:
        if i.isdigit():
            return True
        
def length(s):
    if len(s) > 8:
        return True

st=input("Enter Your Password: ")
if upper(st) and lower(st) and digit(st) and length(st):
    print("Password is Right ")
else:
    print("Password Structure Wrong : ")
