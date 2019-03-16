for _ in range(int(input())):
    n=int(input())
    alice=list(map(int,input().split()))
    bob=list(map(int,input().split()))
    res=sum(alice)-max(alice)-sum(bob)+max(bob)
    if res>0: print('Bob')
    elif res==0: print('Draw')
    else: print('Alice')
