t=int(input())
for _ in range(t):
    n=int(input())
    res=n%8
    if res==0:
        print(n-1,'SL',sep='')
    elif res==1:
        print(n+3,'LB',sep='')
    elif res==2:
        print(n+3,'MB',sep='')
    elif res==3:
        print(n+3,'UB',sep='')
    elif res==4:
        print(n-3,'LB',sep='')
    elif res==5:
        print(n-3,'MB',sep='')
    elif res==6:
        print(n-3,'UB',sep='')
    else:
        print(n+1,'SU',sep='')
