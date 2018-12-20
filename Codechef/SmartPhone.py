lst=[]
t=int(input())
for i in range(t):
    lst.append(int(input()))
lst=sorted(lst)
mxx=int(lst[0]*t)
for i in range(1,t):
    if mxx<lst[i]*(t-i):
        mxx=lst[i]*(t-i)
print(mxx)
