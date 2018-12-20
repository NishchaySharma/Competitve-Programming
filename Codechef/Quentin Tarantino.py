t=int(input())
for _ in range(t):
    n=int(input())
    check=[i for i in range(1,n+1)]
    inpt=list(map(int,input().split()))
    if inpt==check:
        print('no')
    else:
        flag=True
        inpt.sort()
        for i in range(n):
            if check[i]!=inpt[i]:
                flag=False
                break
        if flag:
            print('yes')
        else:
            print('no')
