t=int(input())
for _ in range(t):
    n=int(input())
    if n==1:
        print(1)
    elif n==2:
        print(1,2)
    else:
        l=[100,101]
        for i in range(2,n):
            l.append(l[i-1]+1)
        for i in l:
            print(i,end=' ')
        print()
