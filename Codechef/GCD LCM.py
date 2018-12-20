#GCD * LCM = product of the numbers!
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    rep1=a; rep2=b
    while(True):
        if a==0 or b==0:
            break
        elif a>b:
            a%=b
        elif a<b:
            b%=a
    gcd=b if a==0 else a
    lcm=int(rep1*rep2/gcd)
    print(gcd,lcm)
