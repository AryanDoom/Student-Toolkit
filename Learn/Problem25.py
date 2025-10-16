list1=['1','2','3','4','5']
list2=[]
for i in range(len(list1)-1):
   a=int(list1[i+1])-int(list1[i])
   list2.append(a)
print(list2)   

