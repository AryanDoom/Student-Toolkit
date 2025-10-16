
a = str(input("Enter the roll numbers (space in between): "))
n = int(input("Enter n (number of pairs): "))
m = 2 * n

a = a.split()

if len(a) < m:
    print(f" You entered {len(a)} roll numbers, but I need at least {m} to make {n} pairs.")
else:
    x = a[0:n]      
    y = a[n:m]      
    listf = []
    for i in range(n):
        listf.append(x[i])  
        listf.append(y[i])  
    print(" Interleaved roll numbers:", listf)

