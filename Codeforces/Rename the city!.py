for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if l.count(1)>=l.count(-1):
        print('YES')
    else:
        print('NO')
