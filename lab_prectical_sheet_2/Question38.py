"""
Write a program that display following output:
SHIFT
HIFTS
IFTSH
FTSHI
TSHIF
SHIFT

"""

st=input("Enter the String ")
l1 =[]
for i in st:
    l1.append(i)

for j in range(len(l1)):
    a=l1[0]
    del l1[0]
    l1.append(a)
    res=''.join(l1)
    print(res)


