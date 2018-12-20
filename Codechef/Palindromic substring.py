t=int(input())
for i in range(t):
    a=input()
    b=input()
    flag=0
    for j in a:
        for k in b:
            if j==k:
                flag=1
                break
    if flag==0:
        print('No')
    else:
        print('Yes')
