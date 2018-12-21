'''
    Using binomial coefficient
'''
hold,current={0:1},0
def fact(n:int)->int:
    global hold,current
    if current<n:
        for i in range(current+1,n+1):
            hold[i]=hold[i-1]*i
        current=n
    return hold[n]
def comb(n:int,r:int)->int:
    return fact(n)//(fact(n-r)*fact(r))
for _ in range(int(input())):
    n=int(input())
    print(comb(2*n,n)//(n+1))
