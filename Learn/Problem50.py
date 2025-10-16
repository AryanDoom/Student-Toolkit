a=(input("Enter the string:"))
a=a.rstrip()
last_space=a.rfind(" ")
last_word=a[last_space + 1:]
b=len(last_word)
print("The lenght of the last word is",b)