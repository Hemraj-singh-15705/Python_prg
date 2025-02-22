"""
Compute the sum up to n terms in the series
1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n
where n is a positive integer and input by user.
"""


n=int(input("Enter the range :"))
even_sum =0
odd_sum = 0
for i in range(1,n+1):
    if i%2 == 0:
        even_sum += 1/i
    else:
        odd_sum += 1/i
    
print(f"total Compute Sum : {even_sum-odd_sum}")