list1=[1,2,3,4,5,6,7,8,9,0,11,12,13]
list2=[11,12,13,14,15,16,17]
list4=list()
list5=list()
list6=list()
list7=list()
a=max(len(list1),len(list2))
list3=list1+list2
set1=set(list3)
print(set1)
for i in range(a):
    if list1[i] in list2:
        list4.append(list1[i])
print(list4)    
for i in range(len(list1)):
    if list1[i] not in list4:
        list5.append(list1[i]) 
print(list5)    
for i in range(len(list2)):
    if list2[i] not in list4:
        list6.append(list1[i]) 
list7=list5+list6   
print(list6)           