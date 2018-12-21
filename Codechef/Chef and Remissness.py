t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a>b:
        print(a,b+a)
    else:
        print(b,a+b)
