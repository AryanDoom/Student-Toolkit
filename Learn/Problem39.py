a=int(input("Enter the number of rows of the pyramid:"))
for i in range(1,a+1):
    print("*"*i)
b=int(input("Enter the number of rows needed:"))
for i in range(1, b + 1):
    print(" " * (b - i) + "*" * (2 * i - 1))
c=int(input("Enter the number of rows needed:"))
for i in range(1, c + 1):
    print(" " * (c - i) + "*" * (2 * i - 1))
for j in range(1, c + 1):
    print(" " * (j -1) + "*" * (2 * (c - j) + 1))
d=int(input("Enter the side of the sqaure:"))
print("*" * d)
for k in range(d-2):
    print("*" + " " * (d - 2) + "*")
print("*" * d)
def num_patter(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
num_patter(int(input("Enter the number of rows needed:")))
       