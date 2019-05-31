for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    if len(set(l)) == n: print('No')
    else: print('Yes')
