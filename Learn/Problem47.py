s=str(input("Enter the brackets"))
sum=0 
a=0
b=0

if '(' in s:
    sum = sum + 7
if ')' in s:
    sum = sum + 7
if '[' in s:
    sum = sum + 13
if ']' in s:
    sum = sum + 13
if '{' in s:
    sum = sum + 19
if '}' in s:
    sum = sum + 19  
if sum % 78 != 0:
    print(" not valid")  
    a = a + 1  
if sum % 52 != 0:
    print(" not valid")
    a = a + 1
if sum % 64 != 0:
    print(" not valid")
    a = a + 1
if sum % 40 != 0:
    print(" not valid")   
    a = a + 1 
if sum % 14 != 0:
    print(" not valid")
    a=a+1
if sum  % 26 != 0:
    print(" not valid")
    a=a+1
if sum % 38 != 0:
    print(" not valid")
    a=a+1         
if a>1:
    print("FINALLY VALIDDDDDDDDDDD")