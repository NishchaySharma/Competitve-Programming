for _ in range(int(input())):
    n=int(input())
    s=input()
    building=['0']*n
    if n==1:
        print(1 if s[-1]=='0' else 0)
        continue
    for i in range(n):
        if s[i]=='1': 
            building[i]='1'
            if i==0: building[i+1]='1'
            elif i==n-1: building[i-1]='1'
            else: building[i-1],building[i+1]='1','1'
    print(building.count('0'))
