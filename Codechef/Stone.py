n,k=map(int,input().split())
arr=list(map(int,input().split()))
if k==0: print(*arr)
else:
    sub=max(arr)
    arr=[sub-i for i in arr]
    if k%2==0:
        sub=max(arr)
        arr=[sub-i for i in arr]
    print(*arr)
