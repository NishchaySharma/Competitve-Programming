def bsearch(arr:list,find:int,start:int,end:int)->int:
    ret=-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]>find:
            end=mid-1
        else:
            ret=mid
            start=mid+1
    return ret
def upper(n:int,r:int)->int:
    res=1
    for i in range(n-r+1,n+1):
        res*=i
    return res
def lower(n:int)->int:
    res=1
    for i in range(2,n+1):
        res*=i
    return res
for _ in range(int(input())):
    n,p,k=map(int,input().split())
    arr=sorted(list(map(int,input().split())))
    ways=0
    for i in range(n-k+1):
        nn=bsearch(arr,arr[i]*p,i+1,n-1)
        nn=nn-i
        if nn!=-1 and nn>=k-1:
            ways+=(upper(nn,k-1)//lower(k-1))
    print(ways%1000000007)
