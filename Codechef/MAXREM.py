n = input()
l = sorted(list(set(map(int,input().split()))))
print(0) if len(l) == 1 else print(l[-2]%l[-1])
