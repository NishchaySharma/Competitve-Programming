def network(n:int,x:int,w:int,b:int)->int:
    if n==1:
        return x
    else:
        return network(n-1,w*x+b,w,b)
t=int(input())
for test in range(t):
    n,minx,maxx=map(int,input().split())
    w,b=[],[]
    for i in range(n):
        tmp1,tmp2=map(int,input().split())
        w.append(tmp1)
        b.append(tmp2)
    sp,nsp,x=0,0,minx
    while x!=maxx:
        if network(n,x,w[i],b[i])%2==0:
            nsp+=1
        else:
            sp+=1
    print(sp,nsp)
