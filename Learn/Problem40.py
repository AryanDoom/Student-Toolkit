d={"roshan":{"maths":100,"phy":90,"chem":95},"dhruva":{"maths":90,"phy":89,"chem":95}}
a=eval(input("Enter the name of the student:"))
if a in d:
    b,c=input("Enter the subject:").lower().split()
    if b and c in d[a]:
        print("Marks obtained:",d[a][b],d[a][c])
        print("Average marks:",((d[a][b]+d[a][c])/2))
    else:
        print("Subject not found")
else:
    print("Student not found")
