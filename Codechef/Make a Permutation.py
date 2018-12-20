t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=list(set(a))
    cnt=len(a)-len(s)
    for i in s:
        if i>n:
            cnt+=1
    print(cnt)
