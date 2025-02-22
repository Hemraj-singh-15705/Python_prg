"""
Find the sum of each row of matrix of size m x n. For example for the following matrix
output will be like this :

2 11 7 12
5 2  9 15
8 3 10 42


Sum of row 1 = 32
Sum of row 2 = 31
Sum of row 3 = 63

"""

m=int(input("Enter the m value : "))
n=int(int(input("Enter the n value : ")))
matrix=[]
for i in range(m):
    l1 = []
    for j in range(n):
        l1.append(int(input("Enter the Matrix Value{m X n} ")))
    matrix.append(l1)

for i in range(m):
    for j in range(n):
        print(matrix[i][j] , end= " ")
    print()

print("Sum of matrix ")
sum=0
for i in range(m):
    for j in range(n):
        sum += matrix[i][j]
    print(sum)
    sum=0
