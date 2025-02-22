import math
a = int(input("Enter the Side of A :"))
b = int(input("Enter the Side of B :"))
c = int(input("Enter the Side of C :"))
p= a+b+c
sp =p/2
sqrta= (sp-a)**(1/2)
sqrtb =(sp-b)**(1/2)
sqrtc =(sp-c)**(1/2)

area= (sp*sqrta*sqrtb*sqrtc)**(1/2)
print(area)