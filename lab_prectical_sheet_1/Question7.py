import random,math
num = int(input("Enter the number where till you want to generate random number : "))
ran = math.floor((random.random()*num)+1)
print(ran)