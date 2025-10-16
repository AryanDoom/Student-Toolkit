a=int(input("Enter the integer:"))
list1=[]
if a<=0:
   print("Invalid input")
for i in range(a):
    if a>=1000:
       print("M",end="")
       a=a-1000
       list1.append("M")
    elif a>=500:
       print("D",end="")
       a=a-500
       list1.append("D")   
    elif a>=100:
       print("C",end="")
       a=a-100
       list1.append("C")
    elif a>=50:
       print("L",end="")
       a=a-50
       list1.append("L")
    elif a>=10:
       print("X",end="")
       a=a-10
       list1.append("X")
    elif a>=5:
       print("V",end="")
       a=a-5
       list1.append("V")
    elif a>1:
       print("I",end="")
       a=a-1
       list1.append("I") 
    elif a==1:
       print("I",end="")
       a=a-1
       list1.append("I")
    elif a==0:
       break  
print("The Roman numeral is:",list1)                         