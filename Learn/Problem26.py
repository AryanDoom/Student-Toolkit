list1=[1,2,3,4,5]
list_int=[]
list_str=[]
list_float=[]

for i in range(len(list1)-1):
    if isinstance(list1[i],int):
        list_int.append(i)
    elif isinstance(list1[i],str):
        list_str.append(i)
    elif isinstance(list1[i],float):
        list_float.append(i)    
print(list_float,list_int,list_str)           
