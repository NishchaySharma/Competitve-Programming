n,q=map(int,input().split())
arr=list(map(int,input().split()))
l,u=min(arr),max(arr)
for _ in range(q):
    tmp=int(input())
    if tmp>=l and tmp<=u : print('Yes')
    else: print('No')
