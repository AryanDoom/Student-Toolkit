list2=[1,3,5,7,9]
list1=[2,4,6,8,10,11,12,13,14,15,16,17,18,19,20]
list3=[]
if  len(list1)>len(list2):
    for i in range(len(list2)):
        list3.append(list1[i])
        list3.append(list2[i])
    for j in range(len(list2),len(list1)):
        list3.append(list1[j])
else:
    for i in range(len(list1)):
        list3.append(list1[i])
        list3.append(list2[i])
    for j in range(len(list1),len(list2)):
        list3.append(list2[j])
print("The merged list is:",list3)        