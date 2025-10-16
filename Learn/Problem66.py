f1=open("writefile.txt","w")
x=str(input("Enter the info:")).lower()
y="stop"
while x!=y:
    f1.write(x+"\n")
    x=input("ENter the info:")
f1.close()    