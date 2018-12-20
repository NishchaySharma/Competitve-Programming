t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=sorted(list(map(int,input().split())))
    res=sum(l)
    div=n
    if k!=0:
        div-=2*k
        for i in range(k):
            res-=l[i]+l[n-i-1]
    print(res/div)
