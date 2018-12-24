n,k=map(int,input().split())
arr=list(map(int,input().split()))
count,k=0,arr[k-1]
for i in arr:
    if i>=k and i>0:
        count+=1
print(count)
