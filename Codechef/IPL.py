n=int(input())
lst=[]
ttl=0
for i in range(n):
    lst.append(int(input()))
    ttl+=lst[i]
cnt=0
pos=0
while cnt<n:
    for i in range(cnt,cnt+4):
        if i<n and lst[pos]>=lst[cnt]:
            pos=cnt;
        cnt+=1
    ttl-=lst[pos]
print(ttl)
