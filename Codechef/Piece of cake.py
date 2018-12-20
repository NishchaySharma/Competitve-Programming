t=int(input())
for test in range(t):
    s=input()
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    flag=1
    for k,v in d.items():
        if v==len(s)/2:
            print('YES')
            flag=0
            break
    if flag==1:
        print('NO')
