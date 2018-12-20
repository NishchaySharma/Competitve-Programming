t=int(input())
for test in range(t):
    s=input()
    if s.count('a')==0 or s.count('b')==0:
        print(0)
    else:
        print(s.count('a')) if s.count('a')<s.count('b') else print(s.count('b'))
