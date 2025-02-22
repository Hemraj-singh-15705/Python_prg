"""
19. Write programs to print following patterns :
1.
        **********
        **********
        **********
        **********
2.
            *
            **
            ***
            ****
            *****
3.
             *
            **
           ***
          ****
         *****
4.
    *
   ***
  *****
 *******
*********
5.
    1
   222
  33333
 4444444
555555555
6.
    1
   212
  32123
 4321234
543212345
"""

print("1 pattern ")
row=int(input("Enter the row : "))
for i in range(1,row+1):
    for j in range(1 , row+1):
        print("*    ", end=" ")
    print()


print(" 2 pattern ")
# row=int(input("Enter the row : "))
for i in range(1,row+1):
    for j in range(1 , i+1):
        print("* ", end=" ")
    print()

print("3 pattern ")

for i in range(1,row):
    for j in range(1,row):
        if row-i>j:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()


print("4 pattern ")



# row = int(input("Enter the number of rows: "))

for i in range(1, row + 1):
    for j in range(row - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()


print("5 pattern ")

for i in range(1, row + 1):
    for j in range(row - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print(i, end="")
    print()


print("6 pattern ")

# row = int(input("Enter the number of rows: "))

for i in range(1, row + 1):
    for j in range(row - i):
        print(" ", end="")
    for k in range(i, 0, -1):
        print(k, end="")
    for l in range(2, i + 1):
        print(l, end="")
    print()
