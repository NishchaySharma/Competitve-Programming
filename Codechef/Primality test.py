t=int(input())
for i in range(t):
    n=int(input())
    fact=0
    for j in range(2,int(pow(n,0.5))+1):
        if n%j==0:
            fact+=1
            break
    if fact==0 and n!=1:
        print('yes')
    else:
        print('no')
