def add(a,b):
    c=a+b
    return(c)


def sub(a,b):
    c=a-b
    return(c)

def mul(a,b):
    c=a*b
    return(c)

def div(a,b):
    c=a / b
    return(c)

x=(input("Enter the operation you want to perform(+,-,/,*):"))
y,z=(input("Enter the numbers(spaces in btw):")).split()
y=int(y)
z=int(z)
if x=="+":
    i=add(y,z)
    print(i)

elif x=="-":
    i=sub(y,z)
    print(i)   

elif x=="*":
    i=mul(y,z)
    print(i)

elif x=="/":
    i=div(y,z)
    print(i)  
