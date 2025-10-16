f1 = open("file 2.txt", "r")
f2 = open("hi how are you.txt", "w")  

lines = f1.read().split()

for i in lines:
    if i[0].lower() in "aeiou":  
        print(i, file=f2)

f1.close()
f2.close()