for _ in range(int(input())):
    n,x=map(int,input().split())
    s=input()
    pos,val=n//2 + 1,[0]*(2*n+2)
    val[pos]=1
    for i in s:
        if i=='L': pos-=1
        else: pos+=1
        val[pos]=1
    print(val.count(1))
