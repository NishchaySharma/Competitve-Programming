t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    r=list(map(int,input().split()))
    s=[]
    high=0
    res=0
    for i in range(n):
        if high<l[i]*r[i]:
            high=l[i]*r[i]
            res=i
        elif high==l[i]*r[i]:
            if r[i]>r[res]:
                res=i
    print(res+1)
