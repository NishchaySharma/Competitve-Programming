from math import pow
t=int(input())
for i in range(t):
    total=0
    n=int(input())
    total+=n%10
    n/=pow(10,len(str(n))-1)
    total+=int(n)%10
    print(total)
