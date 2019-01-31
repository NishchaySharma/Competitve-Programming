for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=[]
    for _ in range(n):
        arr.append(list(input()))
    res=0
    for i in range(m):
        tmp=0
        for j in range(n):
            if arr[j][i]=='1': tmp+=1
        res+=(tmp*(tmp-1)//2)
    print(res)
    
