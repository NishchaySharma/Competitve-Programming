t=int(input())
for i in range(t):
    q,p=map(int,input().split())
    if q>1000:
        print('{0:6f}'.format(float(q*p*.9)))
    else:
        print('{0:6f}'.format(float(q*p)))
