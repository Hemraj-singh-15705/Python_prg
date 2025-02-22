"""
 Write a program that reads a string from keyboard and display:
* The number of uppercase letters in the string
* The number of lowercase letters in the string
* The number of digits in the string
* The number of whitespace characters in the string
"""
upper=0
lower=0
digit=0
whitespace=1

st=input("Enter the String : ")
for i in st:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isdigit():
        digit+=1
    elif i == ' ':
        whitespace+=1
    else:
        print("invalid ")
print("Upper case : ",upper)
print("Lower case : ",lower)
print("White Space : ",whitespace)
print("Digit : ",digit)
