"""
Write a program that prompts the user to input a positive integer. It should then
output a message indicating whether the number is a prime number. A prime number is
a number that is evenly divisible only by itself and 1. For example, the number 5 is prime
because it can be evenly divided only by 1 and 5. The number 6, however, is not prime
because it can be divided evenly by I, 2, 3, and 6.
"""

def primeCheck(n):
    for i in range(2,n):
        if n%2==0:
            return 1
    return 0
        
    

n=int(input("Enter the number : "))
if primeCheck(n) == 1:
    print(n,"is not prime number")
else:
    print(n,"is Prime number ")