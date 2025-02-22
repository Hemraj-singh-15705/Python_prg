""" 
Write a program which prompts the user to input principle, rate and time and
calculate compound interest. The formula is :
CI = P(1+R/100)^T - P
"""

principle=int(input("Enter the Principle Value : "))
rate=int(input("Enter the rate : "))
time=int(input("Enter the time : "))
amount=principle*((1+rate/100)**time)
print("Compound Interest : ", amount-principle)
