t=int(input())
for test in range(t):
    n,k=map(int,input().split())
    n_val=list(map(int,input().split()))
    cnt=0
    for i in n_val:
        i+=k
        if i%7==0:
            cnt+=1
    print(cnt)
