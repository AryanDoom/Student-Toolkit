list1=[1,2,3,4,5,6,7,8,9,10]
list2=[11,12,13,14,15,16,17]
list3=[21,22,23,24,25,26,27]
list4=[]
if len(list1)<=len(list2) and len(list1)<=len(list3):
    for i in range(len(list1)):
        list4.append(list1[i]+list2[i]+list3[i])
elif len(list2)<=len(list1) and len(list2)<=len(list3):
    for i in range(len(list2)):
        list4.append(list1[i]+list2[i]+list3[i])
else:
    for i in range(len(list3)):
        list4.append(list1[i]+list2[i]+list3[i])
print("The new list is:",list4)                