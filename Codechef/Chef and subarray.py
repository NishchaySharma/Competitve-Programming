t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    cnt=0
    for i in range(n):
        pro=1
        tot=0
        for j in range(i,n):
            pro*=a[j]
            tot+=a[j]
            if pro==tot:
                cnt+=1
    print(cnt)
