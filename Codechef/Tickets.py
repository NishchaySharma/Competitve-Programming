t=int(input())
for _ in range(t):
    s=list(input())
    if set(s[::2])==set(s[0]) and set(s[1::2])==set(s[1]) and s[0]!=s[1]:
        print('YES')
    else:
        print('NO')
