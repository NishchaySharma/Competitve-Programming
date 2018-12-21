t=int(input())
for _ in range(t):
    n=int(input())
    l=sorted(list(map(int,input().split())))
    tot_n,tot_p=[],[]
    for i in l:
        if i<0:
            tot_n.append(i)
        else:
            tot_p.append(i)
    if len(tot_n)!=0:
        if len(tot_p)!=0:
            res=sum(tot_p)-sum(tot_n)
        else:
            res=abs(sum(tot_n)-2*tot_n[-1])
    else:
        res=sum(tot_p)-2*tot_p[0]
    print(res)
