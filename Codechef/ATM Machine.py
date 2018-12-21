t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    for i in a:
        if k>=i:
            k-=i
            print('1',end='')
        else:
            print('0',end='')
    print()
