dict1={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
a=str(input('Input the roman numeral as a string:')).upper()
b=len(a)
i=0
integer=0
while i<b:
    if i+1<b and dict1[a[i]] > dict1[a[i+1]]:
        integer=dict1[a[i]]+integer
        print(integer)
        i=i+1
    elif i+1<b and dict1[a[i]] < dict1[a[i+1]]:
        bitchass_why_does_this_exists=(dict1[a[i+1]]-dict1[a[i]])  
        integer=integer+bitchass_why_does_this_exists
        i=i+2
    elif i+1<b and dict1[a[i]]==dict1[a[i+1]]:
        c=( dict1[a[i]] + dict1[a[i+1]] )
        integer=integer+c
        i=i+2    
print("The integer value of the roman numeral is:",integer)        
#xlvii   