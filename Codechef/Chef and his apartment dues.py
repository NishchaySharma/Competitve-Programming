for _ in range(int(input())):
    n=int(input())
    months=list(map(int,input().split()))
    zero,pay=0,0
    for i in months:
        if i==1 and zero!=0: pay+=100
        elif i==0: zero+=1; pay+=1100
    print(pay)
