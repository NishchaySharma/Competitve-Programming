t=int(input())
for test in range(t):
    a,b,c,d=map(int,input().split())
    r1,r2=a-c,b-d
    if r1==0:
        if r2<0:
            print('up')
        elif r2>0:
            print('down')
    elif r2==0:
        if r1>0:
            print('left')
        elif r1<0:
            print('right')
    else:
        print('sad')
