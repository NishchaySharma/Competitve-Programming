t=int(input())
for i in range(t):
    s=input()
    flag=0
    for i in s:
        if s.count(i)>1:
            flag=1
            break
    if flag==0:
        print('no')
    else:
        print('yes')
