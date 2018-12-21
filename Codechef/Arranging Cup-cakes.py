t=int(input())
for _ in range(t):
    n=int(input())
    diff=n
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            if diff>abs(n//i - i):
                diff=abs(n//i - i)
                if diff==0:
                    break
    print(diff)
