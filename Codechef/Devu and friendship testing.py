t=int(input())
for _ in range(t):
    n=int(input())
    d=list(map(int,input().split()))
    d2=list(set(d))
    print(len(d2))
