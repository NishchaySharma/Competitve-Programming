t=int(input())
for test in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    pos=int(input())
    element=l[pos-1]
    l=sorted(l)
    print(l.index(element)+1)
