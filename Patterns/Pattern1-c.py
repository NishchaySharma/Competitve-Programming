n = int(input())
space, star = n-1, 1
for i in range(n):
    print(' '*space, end = '')
    print("*"*star)
    star+=1
    space-=1
