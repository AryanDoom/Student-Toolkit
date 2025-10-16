a=int(input("Choose the Range for the digits: "))
b=(input("Choose the type of number even(e),odd(o),both(t)"))
for i in range(1,a+1) :
    if(b=="e") and (i % 2==0):
       print(i,end=" ")
    elif(b=="o") and (num % 2!=0):
       print(i,end=" ")
    elif(b=="t"):
       print(i,end=" ")    

    
   