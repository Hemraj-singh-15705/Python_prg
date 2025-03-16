"""
Write a recursive function that accepts an integer argument and returns the factorial.
"""

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)

n = int(input("Enter the number: "))
factorial = fact(n)
print("Factorial:", factorial)
