"""
Write a program that prompts the user to input a number. Program should display
the corresponding days to the number. For example if user type 1 the output should be
sunday. If user type 7 the output should be saturday.
"""
num=int(input("Enter a number : "))
if num ==1:
    print("Sunday")
elif num ==2:
    print("Monday")
elif num == 3:
    print("Tuesday")
elif num == 4:
    print("Wednesday")
elif num == 5:
    print("Thursday")
elif num == 6:
    print("Friday ")
elif num == 7:
    print("Saturday ")
else:
    print("Invalid")