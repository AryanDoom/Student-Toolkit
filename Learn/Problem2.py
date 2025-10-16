from cmath import sqrt


a,b=(input("Enter the numbers of which the sum and square root is to found:")).split()
a=int(a)
b=int(b)
if(a+b<0):
    print("Square root of negative numbers is imaginary")
else:
    s=sqrt(a+b)
    print("The square root of the sum of the two digits is:",s)