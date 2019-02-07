t=int(input())
for test in range(t):
    n=int(input())
    val=input()
    val=list(val)
    cnt=0
    for i in val:
        if i=='1':
            cnt+=1
    print((cnt*(cnt+1))//2)
