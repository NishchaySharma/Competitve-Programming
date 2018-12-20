t=int(input())
for _ in range(t):
    d={chr(i):0 for i in range(97,123)}
    l=list(map(int,input().split()))
    inpt=input()
    for i in range(97,123):
        d[chr(i)]=l[i-97]
    s={chr(i) for i in range(97,123)}
    res=s-set(inpt)   
    tot=0
    for i in list(res):
        tot+=d[i]
    print(tot)
