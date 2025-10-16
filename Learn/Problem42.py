set1={1,2,3,4,5,6,7,8,9,10}
set2={11,12,13,14,15}
set3=set()
for i in set1:
    for j in set2:
        set3.add(i)
        set3.add(j)
        print(set3)
        set3.clear()