og_str=str(input("Enter a string: "))
max_length=0
longest_string_palindrome=""
for i in range(len(og_str)):
    for j in range(i,len(og_str)):
        substring=og_str[i:j+1]
        if substring==substring[::-1] and len(substring)>max_length:
            max_length=len(substring)
            longest_string_palindrome=substring
print("The longest palindromic substring is:",longest_string_palindrome)
print("The length of the longest palindromic substring is:",max_length)

