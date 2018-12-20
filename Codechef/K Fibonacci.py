n,k=map(int,input().split())
l=[1]*k
tmp=k
for i in range(k,n):
    l.append(tmp%1000000007)
    tmp=(2*l[i]-l[i-k])
print(l[n-1])
