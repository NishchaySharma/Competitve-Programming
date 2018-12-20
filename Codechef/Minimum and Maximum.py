t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    cost=min(l)
    cost*=(n-1)
    print(cost)
