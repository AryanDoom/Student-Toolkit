a=int(input("Enter the number:"))
for i in range(2,a):
    if a % (i*i) == 0:
        print("The number is a perfect square")
        break
    else:
        print("The number is not a perfect square")
        break