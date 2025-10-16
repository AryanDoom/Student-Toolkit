a=int(input("Enter the integer:"))
a=str(a)
b=a[::-1]
if b[-1]=="-":
    b=b[:-1]
    b="-"+b
print("The reversed integer is:",b)