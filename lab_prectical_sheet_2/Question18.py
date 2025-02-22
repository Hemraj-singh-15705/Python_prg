"""
The marks obtained by a student in 3 different subjects are input by the user. Your
program should calculate the average of subjects and display the grade. The student
gets a grade as per the following rules:
Average Grade
90-100 A
80-89 B
70-79 C
60-69 D
0-59 F
"""

first=int(input("Enter the first subject number : "))
second=int(input("Enter the second subject number : "))
third=int(input("Enter the third subject number : "))
average=(first+second+third)//3
print("Average =",average)
if average >= 90 and average <= 100:
    print("A")
elif average >= 80 and average <= 89:
    print("B")
elif average >= 70 and average <= 79:
    print("C")
elif average >= 60 and average <= 69:
    print("D")
elif average >= 0 and average <= 59:
    print("F")