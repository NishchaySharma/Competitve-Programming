def gcd(a:int,b:int)->int:
    if a==0 or b==0: return a+b
    else: return gcd(b%a,a)
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    res=arr[0]
    for i in arr[1:]:
        res=gcd(res,i)
        if res==1: break
    print(res)
