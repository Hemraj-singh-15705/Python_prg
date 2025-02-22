"""
A palindrome is a string that reads the same backward as forward. For example, the
words dad, madam and radar are all palindromes. Write a programs that determines
whether the string is a palindrome.
Note: do not use reverse() method

"""
def isPalindrome(s):
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            return False

s=input("Enter  a string :~")
n = len(s)
if(isPalindrome(s) == False):
    print("Given String is not Palindrome : ")
else:
    print("Given String is Palindrome : ")
