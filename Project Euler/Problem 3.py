def findPrime(n:int)->int:
    result=-1
    if n%2==0:
        result=2
        while n%2==0:
            n//=2
    for i in range(3,int(pow(n,0.5))+1,2):
        if n%i==0:
            result=i
            n//=i
    print(n)
    return result
print(findPrime(600851475143))
