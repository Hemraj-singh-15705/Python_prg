"""
3. Find and display the largest number of a list without using built-in function max().
Your program should ask the user to input values in list from keyboard.
"""

l1=[]
for i in range(5):
    l1.append(int(input("Enter the value : ")))
print(l1)


max=0
for i in l1:
    if(i>max):
        max=i
print(i)