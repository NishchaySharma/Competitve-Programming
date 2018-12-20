t=int(input())
for test in range(t):
    n,m=map(int,input().split())
    l=[]
    for i in range(n):
        temp=int(input())
        l.append(temp)
        for j in range(len(l)-1):
            l.append(temp+l[j])
    if m in l:
        print('Yes')
    else:
        print('No')
