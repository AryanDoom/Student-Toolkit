#wap to create a function to find if the given string ia palindrome or not
a=str()
def palindrome(a):
    b=a[::-1]
    if b==a:
        return True
    else:
        return False
print(palindrome("mom"))    