t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=sorted(list(map(int,input().split())),reverse=True)
    d,unique={},[]
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
            unique.append(i)
    if len(unique)<=k:
        print(n)
    else:
        res=0
        for i in range(k):
            res+=d[unique[i]]
        print(res)
