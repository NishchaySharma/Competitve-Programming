t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    res=0
    for i in lst:
        res=res|i
    print(res)
