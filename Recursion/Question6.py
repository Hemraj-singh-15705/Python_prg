"""
Write a recursive function that accepts a decimal integer and display its binary equivalent.
"""

n=int(input("Enter the number :~ "))
res=0
def DecToBin(n):
    if(n == 0):
        return res
    res=res*10+n%2
    DecToBin(n//2)

print("Binary : ",DecToBin(n))