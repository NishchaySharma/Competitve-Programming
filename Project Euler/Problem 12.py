def calFact(num:int)->int:
    if num==1:
        return 1
    ret=2
    for i in range(2,int(pow(num,0.5))+1):
        if num%i==0:
            ret+=2
    if num**0.5==int(num**0.5) and num!=1:
        ret-=1
    return ret
num=1
for i in range(2,1000000):
    if calFact(num)>500:
        break
    else:
        num+=i
print(num)
