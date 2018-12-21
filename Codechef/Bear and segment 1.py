t=int(input())
for _ in range(t):
    s=input()
    count=s.count('1')
    if '1'*count in s and count!=0:
        print('YES')
    else:
        print('NO')
