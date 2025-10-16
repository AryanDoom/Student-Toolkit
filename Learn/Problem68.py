
def len_word():
    x=input("Enter the string:")
    b=x.split()
    for i in b:
        length=len(i)
        if length%2==0:
           print(i,length)
         

len_word()