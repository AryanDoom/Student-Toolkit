print("To find the largest number between 3 number")
a,b,c=input("Enter three different numbers separated by a space:").split()
n1=int(a)
n2=int(b)
n3=int(c)
if(n1>n2):
    if(n1>n3):
        print("The largest number is :",n1)
elif(n2>n1):
    if(n2>n3):
        print("The Largest number is:",n2)
    else:
        print("The largest number is :",n3)     
