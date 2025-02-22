"""
Floyd's triangle is a right-angled triangular array of natural numbers 
"""
row=int(input("Enter the number of row : "))
count=0
for i in range(1, row + 1):
    for j in range(1,i+1):
        count+=1
        print(count,end=" ")
    print()