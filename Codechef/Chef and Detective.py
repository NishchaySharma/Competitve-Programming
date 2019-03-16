n=int(input())
d={i:0 for i in range(1,n+1)}
arr=list(map(int,input().split()))
for i in arr: 
    if i!=0: d[i]+=1
for k in d:
    if d[k]==0: print(k,end=' ')
print()