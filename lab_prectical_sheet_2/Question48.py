"""
 Write a program that prompts the user to input a decimal integer and display its binary equivalent.
"""



decimal= int(input("Enter a decimal integer: "))

# Convert to binary and remove the '0b' prefix
binary = bin(decimal).replace("0b", "")

print(f"The binary equivalent of {decimal} is {binary}")
