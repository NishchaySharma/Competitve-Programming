t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    cnt=0
    for i in range(a,b+1):
        if i<d:
            if i<c:
                cnt=cnt+d-c+1
            else:
                cnt=cnt+d-i
        else:
            break
    print(cnt)
