t=int(input())
for test in range(t):
    s=int(input())
    l=list(map(int,input().split()))
    ss=int(input())
    c=list(map(int,input().split()))
    j=0
    flag=False
    for i in l:
        if c[j]==i:
            j+=1
            if j==ss:
                flag=True
                break
    if flag:
        print('Yes')
    else:
        print('No')
