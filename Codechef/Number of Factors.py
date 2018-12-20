t=int(input())
for test in range(t):
    n=int(input())
    #since every number have atleast 2 factors!
    fact_count=2
    a=list(map(int,input().split()))
    res=1
    for i in a:
        res*=i
    for i in range(2,res//2+1):
        if res%i==0:
            fact_count+=1
    print(fact_count)
