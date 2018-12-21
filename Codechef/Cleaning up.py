t=int(input())
for test in range(t):
    n,m=map(int,input().split())
    total={i for i in range(1,n+1)}
    done=set(map(int,input().split()))
    todo=sorted(list(total.difference(done)))
    for i in range(0,n-m,2):
        print(todo[i],end=' ')
    print()
    for i in range(1,n-m,2):
        print(todo[i],end=' ')
    print()
