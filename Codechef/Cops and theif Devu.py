t=int(input())
for test in range(t):
    m,x,y=map(int,input().split())
    l=sorted(list(map(int,input().split())))
    rng=x*y
    house=[1]*100
    for i in l:
        for j in range(0,rng+1):
            if i-1-j<0:
                break
            elif house[i-1-j]==0:
                break
            else:
                house[i-1-j]=0
            
        for j in range(0,rng+1):
            if i+j-1>99:
                break
            else:
                house[i+j-1]=0
    print(house.count(1))
