"""
Write a recursive function that accepts an integer argument in n. This function returns the nth Fibonacci number. 
Call the function to print fibonacci sequences.
"""

def feb(num):
    if num == 0 or num == 1:
        return num
    else:
        return feb(num-1) + feb(num-2)

num = int(input("Enter the number: "))
print("Fibonacci number:", feb(num))
