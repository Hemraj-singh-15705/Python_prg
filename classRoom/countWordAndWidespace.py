s=(input("Enter a sentence -~ "))
ch = s.strip()
count=0
for i in ch:
    count+=1
print("Count the number of character in manual-> ",count)
print("Count the number of character Using built in fnx-> ",len(ch))

word=1
space=0

for i in ch:
    if i==' ' and i != ch[-1]:
        word+=1
        space+=1
print("word ",word)
print("Space ",space)