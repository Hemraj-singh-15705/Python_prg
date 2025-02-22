num = int(input("Enter a number: ")) 
original_num = num 
sum = 0
while num > 0:
    n = num % 10 
    sum += n ** 3 
    num = num // 10  
if original_num == sum:  
    print(original_num, "is an Armstrong number")
else:
    print(original_num, "is not an Armstrong number")
