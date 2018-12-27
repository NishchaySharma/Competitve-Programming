for _ in range(int(input())):
    s=input()
    flag=True
    for i in range(0,len(s),2):
        if s[i]==s[i+1]:
            flag=False
            break
    if flag:
        print('yes')
    else:
        print('no')
