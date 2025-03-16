"""
Write a recursive function that calculate sum of first n natural numbers.
"""

def sum(n):
    if n==0:
        return n 
    return sum(n-1) 

n=int(input("Enter the number calculate Sum : "))
print("Total Sum of : ",sum(n))