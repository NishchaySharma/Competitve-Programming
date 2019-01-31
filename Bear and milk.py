for _ in range(int(input())):
    n=int(input())
    l=list(input().split())
    flag=True
    if n==1 and l[0]=='cookie': flag=False
    for i in range(n-1):
        if l[i]=='cookie' and l[i+1]!='milk': flag=False; break
    if flag and l[-1]!='cookie': print('YES')
    else: print('NO')
