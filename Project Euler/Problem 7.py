def check_prime(n:int)->bool:
    if n==1:
        return False
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            return False
    return True
count,i=2,1
while True:
    if check_prime(6*i-1):
        count+=1
    if count==10001:
        res=6*i-1
        break
    if check_prime(6*i+1):
        count+=1
    if count==10001:
        res=6*i+1
        break
    i+=1
print(res)
    
