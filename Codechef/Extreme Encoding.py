t=int(input())
for i in range(t):
    a=[]
    b=[]
    size=int(input())
    for j in range(size):
        apnd=int(input())
        b.append(apnd>>16)
        a.append(apnd-(b[j]<<16))
    print('Case '+str(i+1)+":")
    for j in a:
        print(j,end=' ')
    print()
    for j in b:
        print(j,end=' ')
