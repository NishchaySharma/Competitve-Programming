t=int(input())
for test in range(t):
    n,k,s=map(int,input().split())
    tmp,cnt,flag=0,0,True
    for i in range(1,s+1):
        if i%7==0:
            if tmp<k:
                print('-1')
                flag=False
                break
            else:
                tmp-=k
        elif tmp<k:
            if tmp+n-k<0:
                print('-1')
                flag=False
                break
            else:
                tmp+=n-k
                cnt+=1
        else:
            tmp-=k
    if flag:
        print(cnt)
