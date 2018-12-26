def fact(n:int)->int:
    if n==1:
        return 1
    else:
        return n*fact(n-1)
dig=list(str(fact(100)))
res=0
for i in dig:
    res+=int(i)

print(res)
