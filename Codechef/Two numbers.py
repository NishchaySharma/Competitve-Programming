t=int(input())
for test in range(t):
    a,b,n=map(int,input().split())
    if bool(n%2):
        a*=2
    print(a//b if a>b else b//a)
