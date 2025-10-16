list1=['1','2','3','4','5']
len=len(list1)
n=int(input("Enter the number that is to be added:"))
for i in range (0,len-1):
    list1[i] = str(int(list1[i]) + n)
print(list1)    
