n=int(input())
l=list(map(int,input().split()))
if sum(l)==n*(n+1)/2:
    print("YES")
else:
    print("NO")
