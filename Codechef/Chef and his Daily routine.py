t=int(input())
for _ in range(t):
    s=input()
    if len(s)==1:
        print('yes')
    else:
        flag=True
        for i in range(1,len(s)):
            if s[i]>=s[i-1]:
                continue
            else:
                flag=False
                break
        if flag:
            print('yes')
        else:
            print('no')
