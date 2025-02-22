"""
Write a program that prompts the user to input two numbers and display its HCF.
The Highest Common Factor (HCF) also called the Greatest Common Divisor (GCD) of
two whole numbers, is the largest whole number that's a factor of both of them.
"""

def compute_hcf(x, y):
    while(y):
        x, y = y, x % y
    return x


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

hcf = compute_hcf(num1, num2)

print(f"The HCF of {num1} and {num2} is {hcf}")

