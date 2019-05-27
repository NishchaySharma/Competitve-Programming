n = int(input())
s = input()[::-1]
for i in range(n):
    if s[i] == '1':
        print(i)
        break
