def lcm(a:int,b:int)->int:
    return a*b//hcf(a,b)
def hcf(a:int,b:int)->int:
    if a==0 or b==0: return a+b
    else: return hcf(b%a,a)
for _ in range(int(input())):
    n=int(input())
    a=sorted(list(map(int,input().split())))
    flag,pre=False,lcm(a[0],a[1])
    for i in range(n-1):
        for j in range(i+1,n):
            if j==1: continue
            lcm_till=lcm(a[i],a[j])
            if lcm_till<pre: pre=lcm_till
    print(pre)
