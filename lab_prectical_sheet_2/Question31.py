"""
Write a program that accepts a string from user. Your program should count and
display number of vowels in that string.
"""

st=input("Enter A String : ")
count=0
for i in st:
    if i=='a' or i=='e' or i=='i' or i=='o' or i =='u':
        count+=1
print("Total vowel count : ",count)