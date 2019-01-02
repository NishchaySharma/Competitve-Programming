for _ in range(int(input())):
    n=int(input())
    h=list(map(int,input().split()))
    if n%2 and h[n//2]==(n//2)+1 and h[:n//2]==h[n:n//2:-1]: print('yes')
    else: print('no')
