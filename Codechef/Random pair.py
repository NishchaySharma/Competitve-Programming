from math import factorial
def combination(n:int,r:int)->float:
    return factorial(n)/(factorial(n-r)*factorial(r))
t=int(input())
for _ in range(t):
    n=int(input())
    a=sorted(list(map(int,input().split())),reverse=True)
    s=set(a)
    if a[0]==a[1]:
        res=combination(a.count(a[0]),2)/combination(n,2)
    else:
        res=1*a.count(a[1])/combination(n,2)
    print(res)
