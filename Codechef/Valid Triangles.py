t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if a+b+c==180 and bool(a) and bool(b) and bool(c):
        print('YES')
    else:
        print('NO')
