tc=int(input())
for i in range(tc):
    n,k=map(int,input().split())
    res=0
    for j in range(n):
        t,d=map(int,input().split())
        if k>=t:
            k-=t
            continue
        t-=k
        k=0
        res+=t*d
    print(res)
