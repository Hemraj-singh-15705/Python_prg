"""
Write a Python program that accepts a string from user. Your program should create
a new string by shifting one position to left.
For example if the user enters the string 'examination 2021' then new string would be
'xamination 2021e

"""


l1=[]
st=input("Enter a string : ")
for i in st:
    l1.append(i)
a=l1[0]
del l1[0]
l1.append(a)
res=''.join(l1)
print(res)
