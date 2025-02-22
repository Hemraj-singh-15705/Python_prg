"""
Write a program to add first seven terms of the following series using a for loop:

1  + 2  + 3  +..........
1! + 2! + 3! +..........
"""

import math 


def fact(n):
    return math.factorial(n)


end=int(input("Enter the end point number : "))
sum=0
for i in range(1,end+1,1):
    sum+= i/fact(i)


print("Total Sum =",sum)