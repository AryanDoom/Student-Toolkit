ran=int(input("Enter the range of number:"))
for i in range(1,ran+1):
    if (i % 3 ==0):
        print("FIZZ")
        if (i % 5==0):
            print("BUZZ")
    else:
        print(i)    