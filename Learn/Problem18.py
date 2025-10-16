a=int(input("Enter the number till where the Armstron numbers are required :"))
counter=0
for x in range(1,a+1):
    b=str(x)
    c=len(b)
    sum=0
    for i in b:
        sum+=int(i)**c
    if sum==x:
        print(x)    
    else:
        counter=counter+0    
if counter==a:
    print("No Armstrong NUmbers in this range")
        
    