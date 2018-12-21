def fact(a:int,b:int)->int:
    if a==0:
        return b
    else:
        return fact(b%a,a)
t=int(input())
for test in range(t):
    l=list(map(int,input().split()))
    n=l.pop(0)
    res=l[0]
    for i in range(1,n):
        if res==1:
            break
        res=fact(res,l[i])
    for i in l:
        print(i//res,end=' ')
    print()
