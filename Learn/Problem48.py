s=str(input('STRING ENTER BRACKET:'))
if len(s)==2:
    for i in range(len(s)):
        if s[i]=='(' and s[i+1]==')' :
           print("valid")
           break
        elif s[i]=='{' and s[i+1]=='}' :   
           print("valid")
           break
        elif s[i]=='[' and s[i+1]==']' :
            print("valid")
            break
elif len(s)==1:
    print("NOT Valid")
elif len(s)==0:
    print("no brackets given therefore valid")
elif len(s)>2:
    sum = 0
    if '(' in s: sum += 7
    if ')' in s: sum += 7
    if '[' in s: sum += 13
    if ']' in s: sum += 13
    if '{' in s: sum += 19
    if '}' in s: sum += 19
    valid = 0
    if sum % 78 == 0: valid += 1
    if sum % 52 == 0: valid += 1
    if sum % 64 == 0: valid += 1
    if sum % 40 == 0: valid += 1
    if sum % 14 == 0: valid += 1
    if sum % 26 == 0: valid += 1
    if sum % 38 == 0: valid += 1
    if valid >= 2:
       print("FINALLY VALIDDDDDDDDDDD")
    else:
       print("Not valid")

