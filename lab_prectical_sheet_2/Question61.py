"""
22. Write a program to compute cosine of x. The user should supply x and a positive
integer n. We compute the cosine of x using the series and the computation should use
all terms in the series up through the term involving xn
cos x = 1 - x2/2! + x4/4! - x6/6! .....
"""


import math 
cos=0
count=0
sum=0
n=int(input("Enter the number : "))
for i in range(n+1):
    if i%2==0:
        cos=i**i/math.factorial(i)
        if count % 2 == 0:
            sum +=cos
            count +=1
        else:
            sum -= cos
            count +=1

print("Total sum :~ ",sum)