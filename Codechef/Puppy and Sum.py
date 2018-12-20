t=int(input())
for i in range(t):
    d,n=map(int,input().split())
    for j in range(d):
        tot=0
        for i in range(1,n+1):
            tot+=i
        n=tot
    print(n)
