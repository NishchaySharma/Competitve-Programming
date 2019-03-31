n=int(input())
permute=list(map(int,input().split()))
visited,flag=[0]*n,False
store,tmp=[],[]
while True:
    for i in range(n):
        if visited[i]==0:
            visited[i]=1
            start=i+1
            move=i+1
            flag=True
            break
    if not flag: break
    tmp.append(move)
    #print(move,end=' ')
    move=permute[move-1]
    while True:
        tmp.append(move)
        #print(move,end=' ')
        visited[move-1]=1
        if move==start: 
            flag=False
            store.append(tmp[:])
            tmp=[]
            #print()
            break
        move=permute[move-1]
print(len(store))
for i in store:
    print(*i)
