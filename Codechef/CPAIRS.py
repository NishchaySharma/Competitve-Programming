for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    inc, tot = 0, 0
    for i in l:
        if i%2 == 0: inc += 1
        else: tot += inc
    print(tot)
