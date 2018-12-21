n=[137,1315,73,136,255,1384,16385]
power=[2**i for i in range(15)]
for j in n:
    store=[]
    for i in power[::-1]:
        if i<=j:
            j-=i
            store.append(i)
    print(sum(store),"=",end='')
    for i in store:
        print(i," + ",end='')
    print()
