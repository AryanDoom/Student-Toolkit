a=int(input("Enter the number:"))

b=str(a)

c=len(b)
sum=0
counter=0
for i in b:
    sum+=int(i)**c
if sum==a:
    print("The given number is an Armstrong number")    
else:
    print("Not an Armstrong Number")