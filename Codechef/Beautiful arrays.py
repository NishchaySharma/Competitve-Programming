t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    unique=list(set(a))
    d={i:0 for i in unique}
    size=len(unique)
    flag=True
    for i in range(size-1):
        for j in range(i+1,size):
            if unique[i]*unique[j] not in d:
                flag=False
                break
    if flag:
        print('yes')
    else:
        print('no')
