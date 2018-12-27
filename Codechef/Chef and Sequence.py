for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=sorted(list(map(int,input().split())))
    if n-arr.count(1)<=k:
        print('YES')
    else:
        print('NO')
