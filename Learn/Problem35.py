a=int(input("Enter the integer:"))
b=1
power=0
while b<a:
    b=(b*2)
    power=power+1
if b==a:
    print("The given integer is a power of 2 and the power is of the degree",power)    
else:
    print("Given integer is not an exponent of 2")    
