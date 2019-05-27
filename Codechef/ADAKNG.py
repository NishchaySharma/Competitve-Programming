for _ in range(int(input())):
    r, c, k = map(int,input().split())
    print((min(r - 1, k) + min(8 - r, k) + 1)  * (min(c - 1, k) + min(8 - c, k) + 1))
