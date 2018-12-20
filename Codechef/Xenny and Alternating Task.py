t=int(input())
for _ in range(t):
    n=int(input())
    xenny=list(map(int,input().split()))
    yana=list(map(int,input().split()))
    res1=sum(xenny[::2]+yana[1::2])
    res2=sum(xenny[1::2]+yana[::2])
    print(res1 if res1<res2 else res2)
