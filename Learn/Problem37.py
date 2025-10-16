a=int(input("Enter the target number:"))
b=int(input("Enter the maximum integer:"))
sum=0
c=a-b
if c in range(1,b+1):
    print("The pair is as such","(",c,",",b,")")
else:
    print("Such pair does not exist")    