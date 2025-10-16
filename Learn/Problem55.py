#write the program to copy the contents from 1 file to another
f1=open("hi how are you.txt")
f2=open("file 2.txt","w")
lines=f1.read()
for i in lines:
    f2.write(i)

