with open('listin.txt','r') as file1:
    n=int(file1.readline())
    maxx,d=0,{}
    for _ in range(n):
        a,b=map(int,file1.readline().split())
        if a in d:
            d[a]+=1
        else:
            d[a]=1
        if b in d:
            d[b]+=1
        else:
            d[b]=1
        if maxx<max(d[a],d[b]):
            maxx=max(d[a],d[b])
    res=[]
    for k,v in d.items():
        if v==maxx:
            res.append(k)
    with open('listout.txt','w') as file2:
        for i in sorted(res):
            file2.write(str(i)+'\n')
