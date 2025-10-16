from collections import Counter
s=str(input("str1:"))
t=str(input("str2:"))


if Counter(s)==Counter(t):
    print("These are anagrams TRUE")
else:
    print("Not anagrams FALSE")    