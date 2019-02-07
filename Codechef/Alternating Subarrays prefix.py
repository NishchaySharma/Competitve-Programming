def checkalter(a1:int,a2:int):
    if (a1==0 and a2!=0) or (a1!=0 and a2==0):
        return True
    if (a1>0 and a2<0) or (a1<0 and a2>0):
        return True
    return False
t=int(input())
for test in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    i=0
    while i<n-1:
        tot=1
        while i<n-1 and checkalter(a[i],a[i+1]):
            tot+=1
            i+=1
        while tot!=0:
            print(tot,end=' ')
            tot-=1
        i+=1
    if i==n-1:
        print(1)
    else:
        print()
