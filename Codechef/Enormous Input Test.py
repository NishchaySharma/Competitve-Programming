n,k=input().split()
n=int(n)
k=int(k)
cnt=0
for i in range(n):
    val=int(input())
    if val%k==0:
        cnt+=1
print(cnt)
