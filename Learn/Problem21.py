num=int(input("Enter the number which is to be checked:"))
num_str=str(num)
num_str_rev=num_str[::-1]
if num_str_rev==num_str:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")    