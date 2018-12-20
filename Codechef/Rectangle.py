t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    l=sorted(l)
    if l[0]==l[1] and l[2]==l[3]:
        print('YES')
    else:
        print('NO')
