"""
Write a program that reads two integers from keyboard and calculate the greatest common divisor (gcd) using recursive function.
"""

def gcd(num1,num2):
    if num2 ==0:
        return num1
    else:
        num1,num2=num2,num1 % num2
        return gcd(num1,num2)

num1=int(input("Enter the number first : "))
num2=int(input("Enter the number Second : "))
print("Greatest Common Divisor : ",gcd(num1,num2))