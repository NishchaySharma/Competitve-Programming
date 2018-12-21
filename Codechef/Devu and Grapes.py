t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    g=list(map(int,input().split()))
    res=0
    for i in g:
        tmp=i%k
        if i>k:
            res+=min(tmp,k-tmp)
        else:
            res=res+k-i
    print(res)
