"""
Write a program that prompts the user to input number of calls and calculate the
monthly telephone bills as per the following rule:
Minimum Rs. 200 for up to 100 calls.
Plus Rs. 0.60 per call for next 50 calls.
Plus Rs. 0.50 per call for next 50 calls.
Plus Rs. 0.40 per call for any call beyond 200 calls.
"""
call=int(input("Enter the number of calls : "))
if call < 100:
    print("bill is ",200)
elif call > 100 and call <= 150:
    print("Bill ",200+((150-call)*.60))
elif call > 150 and call <= 200:
    print("Bill ",230+((200-call)*.50))
elif call > 200:
    print("Bill ",255+((call-200)*.40))
else:
    print("wrong choice ")