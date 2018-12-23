def satisfy(x:int)->bool:
    return (x//k)*(x%k)==n
n,k=map(int,input().split())
hold,flag=[],True
for a in range(1,int(n**0.5)+1):
    b=n/a
    if int(b)==b:
        x1=a*k+b
        x2=b*k+a
        if satisfy(x1):
            flag=False
            print(int(x1))
            break
        elif satisfy(x2):
            hold.append(x2)
            flag=True
if flag:
    print(int(min(hold)))
