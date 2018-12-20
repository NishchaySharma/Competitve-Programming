'''
    Ugly numbers are those numbers whose only prime factors are 2,3 or 5
    by convention assuming 1 is included.
    Solving using Dynamic Programming.
'''
ugly=[]
def all_possibilities()->None:
    global ugly
    ugly,v2,v3,v5=[1],0,0,0
    for j in range(1,10001):     # 1 is already in the list
        ugly2=ugly[v2]*2
        ugly3=ugly[v3]*3
        ugly5=ugly[v5]*5
        smallest=min(ugly2,ugly3,ugly5)
        ugly.append(smallest)
        if smallest==ugly2:
            v2+=1
        if smallest==ugly3:
            v3+=1
        if smallest==ugly5:
            v5+=1     
all_possibilities()
for _ in range(int(input())):
    n=int(input())
    print(ugly[n-1])     
