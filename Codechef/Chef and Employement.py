for _ in range(int(input())):
    size,extra=map(int,input().split())
    l=sorted(list(map(int,input().split())))
    for _ in range(extra):
        l.append(1000)
    print(l[(size+extra)//2])
