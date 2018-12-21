t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    n1=int(a**0.5)
    n2=int((4*b+1)**0.5 - 1)//2
    if n1>n2:
        print('Limak')
    else:
        print('Bob')
