t=int(input())
for i in range(t):
    c,d,l=map(int,input().split())
    if l%4==0 and l!=0:
        if 2*d>=c:
            if l>=d*4 and l<=(c+d)*4:
                print('yes')
            else:
                print('no')
        else:
            if l>=(c-d)*4 and l<=(c+d)*4:
                print('yes')
            else:
                print('no')
    elif c==0 and d==0 and l==0:
        print('yes')
    else:
        print('no')
