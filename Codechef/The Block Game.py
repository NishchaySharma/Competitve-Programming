t=int(input())
for i in range(t):
    n=int(input())
    print('wins') if n==int(str(n)[::-1]) else print('losses')
