str1="""sanskrit — Kalidasa — Shakuntala  
english — R. K. Narayan — Malgudi Days  
kannada — Kuvempu — Ramayanadarshanam  
sanskrit — Bhasa — Swapnavasavadatta  
kannada — Kuvempu — Malegalalli Madumagalu  
english — R. K. Narayan — Dateless Diary  
kannada — Karanta — Chomana Dudi  
sanskrit — Bana — Harshacharita  
kannada — Karanta — Sarasatamanna Samadhi  
sanskrit — Kalidasa — Malavikagnimitra  
sanskrit — Kalidasa — Raghuvamsha  
sanskrit — Bana — Kadambari  
sanskrit — Bhasa — Pratinayogandharayan"""
str1_split=str1.split("\n")
len_str1=len(str1_split)
print(len_str1)


lang_set=set()
b=str()
for i in range(len(str1_split)):
    a=str1_split[i]
    b=a.split()
    c=b[0:1:1]
    c=str(c)
    lang_set.add(c)
print(lang_set) 
print(len(lang_set))   
    
sans_num=0
eng_num=0
kan_num=0
for i in range(len(str1_split)):
    a=str1_split[i]
    b=a.split()
    c=b[0:1:1]

    if c==['sanskrit']:
        sans_num+=1
    elif c==['kannada']:
        kan_num+=1
    else:
        eng_num+=1
print("No of Sanskrit books:",sans_num,"\n","Number of English books:",eng_num,"\n","Number of Kannad books:",kan_num)


for i in range(len(str1_split)):
    a=str1_split[i]
    b=a.split()
    c=b[0:1:1]
    c=str(c)
    d=b[-1]
    if c=="['sanskrit']":
        print("The book is :",c,d)
    elif c=="['kannada']":
        print("The book is :",c,d)
    else:
        print("The book is :",c,d)


for i in range(len(str1_split)):
    a=str1_split[i]
    b=a.split()
    c=b[0:1:1]
    c=str(c)
    d=b[-1]
    e=set()
    f=b[2:3:1]
    if c=="['sanskrit']":
        print()

    elif c=="['kannada']":
        print("The book is :",c,d)
    else:
        print("The book is :",c,d)

                