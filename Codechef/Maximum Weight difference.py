t=int(input())
for test in range(t):
    n,k=map(int,input().split())
    w=list(map(int,input().split()))
    w=sorted(w)
    tot1,tot2,tot3=0,0,sum(w)
    for i in range(k):
        tot1+=w[n-i-1]
        tot2+=w[i]
    res2=abs(tot3-2*tot1)
    res1=abs(tot3-2*tot2)
    print(res2) if res2>res1 else print(res1)
