t=int(input())
for _ in range(t):
    n=int(input())
    a=sorted(list(map(int,input().split())),reverse=True)
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    res,flag=-1,False
    for k,v in d.items():
        if v>=4 and res==-1:
            res=k*k
            flag=True
            break
        elif v>=2:
            if res==-1:
                res=k
            else:
                res*=k
                flag=True
                break
    if res!=-1 and flag:
        print(res)
    else:
        print(-1)
        
