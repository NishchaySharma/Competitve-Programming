hold={1:0}
def calculate(n:int)->int:
    len=0
    global hold
    if n not in hold:
        if n%2==0:
            hold[n]=1+calculate(n//2)
        else:
            hold[n]=1+calculate(n*3+1)
    return hold[n]
maxx=0
for i in range(2,1000001):
    if calculate(i)>maxx:
        maxx=calculate(i)
        res=i
print(res)
