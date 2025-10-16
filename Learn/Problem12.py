a=int(input("Enter the number of rows needed:"))
for i in range(1, a + 1):
    print(" " * (a - i) + "*" * (2 * i - 1))

