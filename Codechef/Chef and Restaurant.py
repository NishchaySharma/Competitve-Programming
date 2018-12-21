t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    stack=[]
    flag=True
    stack.append(a[0])
    for i in range(1,n//2):
        if a[i]==stack[-1] or a[i]==stack[-1]+1:
            stack.append(a[i])
        else:
            flag=False
            break
    if flag:
        for i in range(n//2,n):
            if a[i]==stack[-1]:
                stack.pop()
            else:
                flag=False
                break
        if flag:
            print('yes')
        else:
            print('no')
    else:
        print('no')
        
        
