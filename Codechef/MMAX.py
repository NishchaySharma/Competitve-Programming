for _ in range(int(input())):
    n = int(input())
    k = int(input())
    if k>=n:
        if k%n == n-(k%n): print((k%n*2) - 1)
        else: print(2*min(n-(k%n), k%n))
    elif k>n/2: print(2*(n-k))
    else: print(2*k)
