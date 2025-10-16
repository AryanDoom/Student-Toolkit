nums = input("Enter integers separated by space: ").split()
nums = [int(x) for x in nums]
r = []
sum = 0
for num in nums:
    sum += num
    r.append((num,sum))
print("Running sum as tuples:",r)

