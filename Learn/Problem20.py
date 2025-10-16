a=int(input("Enter the swapping number:"))
b=str(a)
c=list(b)
c[0],c[-1]=c[-1],c[0]
d=''.join(c)
print(d)
