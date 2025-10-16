str1=input("Enter the string:").lower()
a=("a,e,i,o,u")
vowel=0
consonant=0
for i in range(len(str1)):
    if str1[i] in a:
        vowel+=1
    else:
        consonant+=1  
print(vowel)
print(consonant)          




