"""
Write a recursive function that accepts a number as its argument and returns the sum of digits.
"""
def sum(num):
    if num == 0:
        return 0
    else:
        return (num %10) + sum(num//10)
    
num=int(input("Enter the digit for sum "))
print("Sum of total digit :", sum(num))