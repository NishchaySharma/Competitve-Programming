t=int(input())
for i in range(1,t+1):
    l,k=map(int,input().split())
    if k<=l:
        res=l-k+1
        res=res*(res+1)//2
        print('Case '+str(i)+':',res)
    else:
        print('Case '+str(i)+': 0')
