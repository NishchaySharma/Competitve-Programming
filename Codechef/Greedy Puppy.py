t=int(input())
for test in range(t):
    pre=0
    n,k=map(int,input().split())
    for i in range(1,k+1):
        pre=n%i if n%i>pre else pre
    print(pre)
