def gcd(a:int,b:int)->int:
    if a==0 or b==0: return a+b
    else: return gcd(b,a%b)
for _ in range(int(input())):
    n,a,b,k=map(int,input().split())
    if n//a + n//b - 2*(n//((a*b)//gcd(a,b)))>=k: print('Win')
    else: print('Lose')
