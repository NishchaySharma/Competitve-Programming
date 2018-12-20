t=int(input())
for test in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(n-1,0,-1):
        a[i]-=a[i-1]
    cnt=0
    for i in range(n):
        if b[i]<=a[i]:
            cnt+=1
    print(cnt)
