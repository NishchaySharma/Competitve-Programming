t=int(input())
for i in range(t):
    n=int(input())
    l=[100,50,10,5,2,1]
    cnt=0
    for i in l:
        if n>=i:
            a=n//i
            cnt+=a
            n-=i*a
    print(cnt)
