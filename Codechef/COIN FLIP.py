def gen(n,i,q):
    if n%2==0:
        flip=int(n/2)
    else:
        flip=int(n/2)+1
    return flip

t=int(input())
for i in range(t):
    g=int(input())
    for j in range(g):
        i,n,q=input().split()
        n=int(n)
        i=int(i)
        q=int(q)
        flip=gen(n,i,q)
        if i==q:
            print(n-flip)
        else:
            print(flip)
