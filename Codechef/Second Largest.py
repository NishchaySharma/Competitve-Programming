t=int(input())
for i in range(t):
    lst=[]
    a,b,c=input().split(' ')
    a=int(a)
    b=int(b)
    c=int(c)
    lst.extend([a,b,c])
    lst=sorted(lst)
    print(lst[1])
