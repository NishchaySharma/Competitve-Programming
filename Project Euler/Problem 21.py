store,res={},0
def facts(n:int)->int:
    count=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0: count=count+i+n//i
    return count-n
for a in range(1,10001):
    if a not in store:
        b=facts(a)
        if a==facts(b) and a!=b:
            res+=a+b
            store[a],store[b]=1,1
print(res)
