list=[1,2,3,4,5,6,7,8,9,10]
list_4=[]
list_not4=[]
for i in list:
    if (i % 4 == 0):
        list_4.append(i)
list_not4=[item for item in list if item not in list_4]
print(list_4)
print(list_not4)  