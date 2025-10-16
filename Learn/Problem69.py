a=str(input("Enter the first word:"))
b=str(input("Enter the second word:"))
c=list()
def common(a,b):
   
    a=list(a)
    b=list(b)
    
    for i in range(len(a)):
        if a[i] in b:
            c.append(a[i])
    return(c)
common(a,b)
print(c)