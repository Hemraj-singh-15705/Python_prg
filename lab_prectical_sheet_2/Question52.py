"""
Write a program to enter the numbers till the user wants and at the end it should
display the count of positive, negative and zeros entered.
"""

d1=[]
n=int(input("Enter the range : "))
for i in range(n+1):
    a=int(input("Enter the value : "))
    d1.append(a)


zero = 0
positive = 0
negative = 0


for i in d1:
    if i == 0:
        zero+=1
    elif i < 0:
        negative+=1
    elif i > 0:
        positive+=1

print("positive count ",positive)
print("Negative count :",negative)
print("Zero count : ",zero)