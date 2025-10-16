a,b=(input("Enter one of the point of the line seperated by a space")).split()
c,d=(input("Enter the second point of the line seperated by a space ")).split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if(a==b):
    print("Division by zero in an Mathematical error, slope tends to infinty")
else :
    s=(d-b)/(c-a)
    print("The slope of the given line is:",s)