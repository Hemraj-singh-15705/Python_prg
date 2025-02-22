"""
An Armstrong number of three digits is an integer such that the sum of the cubes of
its digits is equal to the number itself. For example, 371 is an Armstrong number since 
33 + 73 + 13 = 371. Write a program to find all Armstrong number in the range of 0 and 999
"""


def is_armstrong(number):
    digits = [int(digit) for digit in str(number)]
    return sum(digit ** 3 for digit in digits) == number

def find_armstrong_numbers(start, end):
    armstrong_numbers = []
    for number in range(start, end + 1):
        if is_armstrong(number):
            armstrong_numbers.append(number)
    return armstrong_numbers

armstrong_numbers = find_armstrong_numbers(0, 999)
print("Armstrong numbers between 0 and 999 are:", armstrong_numbers)
