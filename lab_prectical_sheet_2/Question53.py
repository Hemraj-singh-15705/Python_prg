"""
Write a program to enter the numbers till the user wants and at the end the
program should display the largest and smallest numbers entered.
"""

d1=[]
n=int(input("Enter the range : "))
for i in range(n+1):
    a=int(input("Enter the value : "))
    d1.append(a)

mininum = min(d1)
maximum = max(d1)

print("Max value : ",maximum)
print("Min value : ",mininum)
