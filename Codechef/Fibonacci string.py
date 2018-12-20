t=int(input())
for test in range(t):
    s=input()
    d,f={},[]
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for k,v in d.items():
        f.append(v)
    size=len(f)
    if size<3:
        print('Dynamic')
    else:
        flag1,flag2=True,True
        f=sorted(f)
        for i in range(2,size):
            if f[i]!=f[i-1]+f[i-2]:
                flag1=False
                break
        f[0]=f[0]+f[1]
        f[1]=f[0]-f[1]
        f[0]=f[0]-f[1]
        for i in range(2,size):
            if f[i]!=f[i-1]+f[i-2]:
                flag2=False
                break
        if flag1 or flag2:
            print('Dynamic')
        else:
            print('Not')
