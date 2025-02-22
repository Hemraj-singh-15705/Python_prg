"""
2. Write a program that accepts a list from user. Your program should reverse the
content of list and display it. Do not use reverse() method.
"""
l1=[]
for i in range(10):
    l1.append(int(input("Enter the value : ")))
print(l1[::-1])