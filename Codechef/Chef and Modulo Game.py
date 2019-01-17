for _ in range(int(input())):
    n,p=map(int,input().split())
    max_mod=n%(n//2 + 1)
    if max_mod==0: print(p*p*p)
    else: print((p-max_mod)**2 + (p-max_mod)*(p-n) + (p-n)**2)
