a=str(input("Enter the list1(spaces in btw):"))
b=str(input("Enter the list2(spaces in btw):"))
a=a.split()
b=b.split()
listf=list()
j=0
x=len(a)
y=len(b)
if len(a)>len(b):
    for i in range(len(b)):
        listf.append(a[i])
        listf.append(b[i])
    listf.extend(a[y:])



if len(a)<len(b):
    for i in range(len(a)):
        listf.append(a[i])
        listf.append(b[i])
    listf.extend(a[x:])




print(listf)