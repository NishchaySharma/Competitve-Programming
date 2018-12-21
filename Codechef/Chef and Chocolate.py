t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    print('Yes' if a*b%2==0 else 'No')
