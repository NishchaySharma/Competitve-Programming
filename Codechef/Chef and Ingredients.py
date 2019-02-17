for _ in range(int(input())):
    n=int(input())
    pre=set(input())
    for _ in range(n-1):
        s=set(input())
        pre=pre.intersection(s)
    print(len(pre))
