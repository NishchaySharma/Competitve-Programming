for _ in range(int(input())):
    n=int(input())
    atk=list(map(int,input().split()))
    dfn=list(map(int,input().split()))
    res=-1
    for i in range(n):
        if dfn[i]>atk[(i+1)%n]+atk[i-1] and res<dfn[i]:
            res=dfn[i]
    print(res)
