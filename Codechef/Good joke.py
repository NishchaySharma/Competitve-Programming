t=int(input())
for _ in range(t):
    n=int(input())
    l=[]
    for _ in range(n):
        tmp=list(map(int,input().split()))
        l.append(tmp)
    res=1
    for i in range(2,n+1):
        res^=i
    print(res)
