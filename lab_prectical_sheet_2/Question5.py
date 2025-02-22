"""
Write a program that accepts seconds from keyboard as integer. Your program
should converts seconds in hours, minutes and seconds. Your output should like this :
Enter seconds: 13400
Hours: 3
Minutes: 43
Seconds: 20
"""

sec=int(input("Enter the second value :~ "))
rem=sec
hours=rem//3600
rem=rem%3600
min=rem//60
rem=rem%60
sec=rem
print("Hours : ",hours)
print("Minutes : ",min)
print("Seconds : ",sec)