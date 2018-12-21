t=int(input())
for test in range(t):
    n,m,k=map(int,input().split())
    if abs(n-m)>k:
        print(abs(n-m)-k)
    else:
        print(0)
