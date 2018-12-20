t=int(input())
for _ in range(t):
    n,b,m=map(int,input().split())
    time,i=0,0
    while n!=0:
        if n%2==1:
            time=time+((n+1)//2)*pow(2,i)*m
            n=n-(n+1)//2
        else:
            time=time+(n//2)*pow(2,i)*m
            n=n-n//2
        i+=1
        if n!=0:
            time+=b
    print(time)
