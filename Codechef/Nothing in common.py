t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l1=set(map(int,input().split()))
    l2=set(map(int,input().split()))
    print(len(l1.intersection(l2)))
