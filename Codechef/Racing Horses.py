t=int(input())
for i in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    s=sorted(s)
    dif=s[1]-s[0]
    for j in range(1,len(s)-1):
         if s[j+1]-s[j]<dif:
             dif=s[j+1]-s[j]
    print(dif)
