"""
Write a program to obtain the first 25 numbers of a Fibonacci sequence. In a
Fibonacci sequence the sum of two successive terms gives the third term. Following are
the first few terms of the Fibonacci sequence:
0 1 1 2 3 5 8 13 21 34 55 89...
"""
a=0
b=1
print(a)
print(b)

for i in range(25):
    sum = a+b
    print(sum ,end="  ")
    a=b 
    b=sum
    