num=int(input("Enter the number for which factor is required:"))
a=1
l=[]
for i in range(1,num+1):
    if (num % i == 0):
        l.append(i)
        a=a+1
    else:
        continue    
print(l)    






