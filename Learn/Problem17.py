import random
a=int(input("Enter the number of random integers you want:"))
for i in range(1,a+1):
    n=random.uniform(1,1000)
    print(f"{n:.0f}")