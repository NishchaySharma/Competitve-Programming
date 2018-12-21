while True:
    n=int(input())
    if n>0:
        lst=list(map(int,input().split()))
        flag=0
        for i in range(n):
            if lst[lst[i]-1]!=i+1:
                flag=1
                break
        if flag==1:
            print('not ambiguous')
        else:
            print('ambiguous')
    else:
        break
