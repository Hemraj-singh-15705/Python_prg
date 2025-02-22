"""
4. Write a program that rotates the element of a list so that the element at the first
index moves to the second index, the element in the second index moves to the third
index, etc., and the element in the last index moves to the first index.
"""


l1=[]
for i in range(5):
    l1.append(int(input("Enter the value : ")))
print(l1)

l1.insert(0,l1[-1])
l1.pop()
print(l1)
