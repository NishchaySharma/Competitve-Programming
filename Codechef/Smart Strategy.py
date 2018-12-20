t=int(input())
for i in range(t):
    n,q=map(int,input().split())
    d=list(map(int,input().split()))
    x=list(map(int,input().split()))
    mull_d=1
    for j in d:
        mull_d*=j
    for j in range(q):
        x[j]//=mull_d
    for j in x:
        print(j,end=' ')
    print()
