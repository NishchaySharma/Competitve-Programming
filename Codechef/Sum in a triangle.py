t=int(input())
for i in range(t):
    n=int(input())
    tmp,l=[],[]
    for j in range(n):
        tmp=list(map(int,input().split()))
        l.append(tmp)
    for j in range(n-1):
        col=n-j-1
        row=n-j-1
        while col>0:
            l[row-1][col-1]+=l[row][col] if l[row][col]>l[row][col-1] else l[row][col-1]
            col-=1
    large=l[0][0]
    for j in l[1:]:
        for k in j:
            if large<k:
                large=k
    print(large)
