a=str(input("Enter the list(use ,):"))
tar=int(input("Enter the target:"))
b=a.split(",")
list1=list(b)
for i in range(len(list1)):
    for j in range(i,len(list1)):
        if int(list1[i]) + int(list1[j]) == tar:
            print(i,j)
            break
    break