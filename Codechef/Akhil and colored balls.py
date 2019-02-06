for _ in range(int(input())):
    s1=input()
    s2=input()
    for i in range(len(s1)):
        if s1[i]==s2[i]: print('W' if s1[i]=='B' else 'B',end='')
        else: print('B',end='')
    print()
