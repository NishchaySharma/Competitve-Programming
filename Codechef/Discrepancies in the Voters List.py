n1,n2,n3=map(int,input().split())
d={}
s=set()
for i in range(n1+n2+n3):
    tmp=int(input())
    if tmp in d:
        s.add(tmp)
    else:
        d[tmp]=1
s=sorted(s)
print(len(s))
for i in s:
    print(i)
