t=int(input())
for test in range(t):
    l=list(map(int,input().split()))
    l.pop(l.index(max(l)))
    print(max(l))
