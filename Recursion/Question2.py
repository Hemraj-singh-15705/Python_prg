"""
. Write a recursive function that accepts two numbers as its argument and returns its power
"""
def power(a,b):
    if b==1:
        return a
    else:
        b-=1
        return a*power(a,b)

a=int(input("Enter the base number : "))
b=int(input("Enter the power number : "))
print("Power :",power(a,b))