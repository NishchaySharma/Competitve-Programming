t=int(input())
for _ in range(t):
    n1,n2,m=map(int,input().split())
    if m==max(n1,n2,m):
        print(abs(n1-n2))
    else:
        for i in range(m,0,-1):
            if n1==0 or n2==0:
                break
            elif n2==0:
                res=0
            if i>min(n1,n2):
                continue
            else:
                n1,n2=n1-i,n2-i
        print(n1+n2)
