"""
Write a program to compute sin x for given x. The user should supply x and a
positive integer n. We compute the sine of x using the series and the computation
should use all terms in the series up through the term involving xn
sin x = x - x3/3! + x5/5! - x7/7! + x9/9!
"""

import math 
sin=0
count=0
sum=0
n=int(input("Enter the number : "))
for i in range(n+1):
    if i%2==1:
        count +=1
        sin=i**i/math.factorial(i)
        if count % 2 == 1:
            sum+=sin
        else:
            sum -= sin

print("Total sum :~ ",sum)
