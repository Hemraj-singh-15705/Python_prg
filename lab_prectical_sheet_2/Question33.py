"""
Write a Python program that accepts a string from user. Your program should create
and display a new string where the first and last characters have been exchanged.
For example if the user enters the string 'HELLO' then new string would be 'OELLH'

"""
l1=[]
st=input("Enter a string : ")
for i in st:
    l1.append(i)
l1[0] ,l1[-1]=l1[-1],l1[0]
res=''.join(l1)
print(res)