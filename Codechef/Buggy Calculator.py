t=int(input())
for _ in range(t):
    a,b=input().split()
    if len(a)>len(b):
        b=b.zfill(len(a))
    elif len(b)>len(a):
        a=a.zfill(len(b))
    a,b=list(a),list(b)
    c=[]
    for i in range(len(a)):
        c.append((int(a[i])+int(b[i]))%10)
    res=''.join(str(i) for i in c)
    print(int(res))
