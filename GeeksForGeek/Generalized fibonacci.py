l=[1,1]
for _ in range(int(input())):
    a,b,c,n,m=map(int,input().split())
    for i in range(n-2):
        #print(l[-1],l[-2])
        l.append(a*l[-1]+b*l[-2]+c)
    print(l[n-1]%m)
