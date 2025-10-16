s = input("Give string")
ns = ""
for c in s:
    if c == 'o':
        ns = ns + "0"
    elif c.isalpha():
        ns = ns + c.upper()
    else:
        ns = ns + c
print(ns)