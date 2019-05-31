def binary_search(start:int, end:int, find:int, l:list)->bool:
    if start <= end:
        mid = (start + end)//2
        if l[mid] == find: return True
        elif l[mid] > find: return binary_search(start, mid - 1, find, l)
        else: return binary_search(mid + 1, end, find, l)
    return False
for _ in range(int(input())):
    n, k = map(int,input().split())
    l = sorted(list(map(int,input().split())))
    flag = True
    for i in range(n-1):
        if binary_search(i+1, n - 1, k - l[i], l):
            flag = False
            break
    if flag: print('No')
    else: print('Yes')
