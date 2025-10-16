u,a,t=input("Enter intial velocity acceleration time of the vehicle:").split()
u=int(u)
a=int(a)
t=int(t)
v=u+(a*t)
s=(u*t)+(a+t^2)/2
print("The final velocity is:",v)
print("The Total Distance travelled is:",s)