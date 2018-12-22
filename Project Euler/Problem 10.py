def check_prime(n:int)->bool:
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            return False
    return True
tot=0
for i in range(2,2000001):
    if check_prime(i):
        tot+=i
print(count)
