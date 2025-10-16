a,b,c=input("Enter Date of Birth in DD MM YYYY format:").split()
a=int(a)
b=int(b)
c=int(c)
if(c<1900):
    print("Age is not plausible")
else:
    y=2025-c
    age=a+(b*30.44)+(y*365.25)   
    print("The amount of days you have lived is approximately:",age) 
