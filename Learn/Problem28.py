list=[]
a=int(input("Enter the lenght of the list that you want:"))
for i in range(0,a):
    b=input("Enter the element:")
    list.append(b)
unique_list=[]
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)
print(len(unique_list))
        
