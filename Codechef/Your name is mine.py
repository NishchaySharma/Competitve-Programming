def check(m:str,f:str)->bool:
    i=0
    for j in f:
        if m[i]==j: i+=1
        if i==len(m): return True
    return False
for _ in range(int(input())):
    m,f=input().split()
    if len(m)>len(f): print('YES' if check(f,m) else 'NO')
    else: print('YES' if check(m,f) else 'NO')
