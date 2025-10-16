haystack = str(input("Enter said haystack as a string:"))
needle = str(input("Enter the needle that is supposed to be found in said haystack:"))
a = len(haystack)
b = len(needle)
if a < b:
    print("-1")
sum = 0
for i in range(a):
    if haystack[i:i+b] == needle:
        print(i)
        sum = sum + 1
if sum < 1:
    print(-1)