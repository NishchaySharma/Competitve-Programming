def gcd(a:int,b:int)->int:
    if a==0 or b==0:
        return a+b
    else:
        return gcd(b,a%b)
res=1
for i in range(2,21):
    res=(res*i)//gcd(res,i)
print(res)
