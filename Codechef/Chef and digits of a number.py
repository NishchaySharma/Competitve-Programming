t=int(input())
for _ in range(t):
    s=input()
    if s.count('1')==1 or s.count('0')==1:
        print('Yes')
    else:
        print('No')
