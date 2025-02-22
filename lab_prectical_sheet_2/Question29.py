"""

 Write a program to add two matrices of size n x m.
 
"""

m=int(input("Enter the m value : "))
n=int(int(input("Enter the n value : ")))
matrix=[]
matrix1=[]

# Matrix 1
print("Enter the matrix 0 element ")
for i in range(m):
    l1 = []
    for j in range(n):
        l1.append(int(input("Enter the Matrix Value {m X n} ")))
    matrix.append(l1)

# Matrix 2
print("Enter the matrix 1 element ")
for i in range(m):
    l2 = []
    for j in range(n):
        l2.append(int(input("Enter the Matrix 1 Value {m X n} ")))
    matrix1.append(l2)

print("Print the 1 matrix ")
for i in range(m):
    for j in range(n):
        print(matrix[i][j], end= " ")
    print()

print("Print the 2 matrix ")
for i in range(m):
    for j in range(n):
        print(matrix1[i][j], end= " ")
    print()

print("Sum of matrix 1 and matrix 2")
for i in range(m):
    for j in range(n):
        print(matrix[i][j]+matrix1[i][j], end= " ")
    print()


