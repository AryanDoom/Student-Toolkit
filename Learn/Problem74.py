a=str()
def string(a):
    lowe=("q,w,e,r,t,y,u,i,o,p,a,sd,f,g,h,j,k,l,z,x,c,v,b,n,m").split()
    u=("Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M").split()
    up1=0
    low1=0
    for i in range(len(a)):
        if a[i] == lowe:
            low1+=1
        else:
            up1+=1
    return(low1,up1) 
print(string("Mom") )