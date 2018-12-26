space={0:1}
def calculate(n:int)->int:
    if n in space:
        return space[n]
    else:
        space[n]=n*calculate(n-1)
        return space[n] 
def combination(n:int,r:int)->int:
    if n not in space:
        calculate(n)
    if r not in space:
        calculate(r)
    return space[n]//(space[n-r]*space[r])
n=int(input())
print(combination(2*n,n))
