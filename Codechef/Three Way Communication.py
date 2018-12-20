t=int(input())
for i in range(t):
    r=int(input())
    chef=list(map(int,input().split()))
    head=list(map(int,input().split()))
    sous=list(map(int,input().split()))
    x,y=0,1
    dist1=pow(pow(chef[x]-head[x],2)+pow(chef[y]-head[y],2),0.5)
    dist2=pow(pow(chef[x]-sous[x],2)+pow(chef[y]-sous[y],2),0.5)
    dist3=pow(pow(head[x]-sous[x],2)+pow(head[y]-sous[y],2),0.5)
    if dist1<=r and dist2<=r or dist1<=r and dist3<=r or dist2<=r and dist3<=r:
        print('yes')
    else:
        print('no')
