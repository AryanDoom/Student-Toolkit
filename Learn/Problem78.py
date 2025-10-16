jewels=set("a,A,b")
stones="aAAbcccadddaA"
sum1=0
for i in range(len(stones)):
    if stones[i] in jewels:
        sum1+=1
print(sum1)        
               