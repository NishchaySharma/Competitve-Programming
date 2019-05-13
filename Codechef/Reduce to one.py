fact, present, MOD = {1:1}, 1, 1000000007
def compute(n:int)->int:
    global present, MOD
    if n+1 > present:   
        for i in range(present+1,n+2):  
            fact[i] = ((i%MOD)*(fact[i-1]%MOD))%MOD
        present = n+1
    return fact[n+1]-1
for _ in range(int(input())):
    n = int(input())
    print(compute(n))
