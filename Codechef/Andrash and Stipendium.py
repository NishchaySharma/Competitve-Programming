for _ in range(int(input())):
    fail,full,n,h,flag=False,False,int(input()),list(map(int,input().split())),True
    for i in h:
        if i<=2:
            fail=True
            break
        if i==5: full=True
    if sum(h)/n>=4 and full and not fail: print('Yes')
    else: print('No')
