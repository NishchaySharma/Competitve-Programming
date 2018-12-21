t=int(input())
for test in range(t):
    x=input()
    y=input()
    flag=0
    for i in range(len(x)):
        if x[i]==y[i]:
            continue
        elif x[i]=='?' or y[i]=='?':
            continue
        else:
            flag=1
            break
    if flag==0:
        print('Yes')
    else:
        print('No')
