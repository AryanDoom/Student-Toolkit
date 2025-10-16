pattern=str(input("Enter the pattern:"))
map=str(input("Enter the mappings:")).split()

dict1={}
dict2={}

if len(map)!=len(pattern):
    print(False)
else:
    for i in range(len(pattern)):
        char = pattern[i]
        word = map[i]
        if char in dict1:
            if dict1[char] != word:
                print(False)
                break
        else:
            dict1[char] = word
        if word in dict2:
            if dict2[word] != char:
                print(False)
                break
        else:
            dict2[word] = char

    print(True)


