t=int(input())
for test in range(t):
    n,k=map(int,input().split())
    d=list(input().split())
    res,l=[],[]
    for j in range(k):
        a=input().split()
        l+=a
    for i in d:
        if i in l:
            res.append('YES')
        else:
            res.append('NO')
    for i in res:
        print(i,end=' ')
    print()
