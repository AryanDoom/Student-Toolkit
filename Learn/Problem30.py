list1=[]
a=int(input("Enter the no of elements in the range:"))
for i in range(a):
    b=i 
    list1.append(b)
List2=[]    
for j in list1:
    if (j % 2 ==0 and j % 3 !=0):
           List2.append(j) 
print("The new list is:",List2)           