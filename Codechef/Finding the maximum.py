t=int(input())
for _ in range(t):
    a=sorted(list(map(int,input().split())))
    a.remove(len(a)-1)
    print(max(a))
