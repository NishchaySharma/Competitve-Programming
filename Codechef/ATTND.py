for _ in range(int(input())):
    n, l, freq = int(input()), [], {}
    for _ in range(n):
        l.append(list(input().split()))
        if l[-1][0] not in freq: freq[l[-1][0]] = 0
        freq[l[-1][0]] += 1
    for i in l:
        if freq[i[0]] != 1: print(i[0],i[1])
        else: print(i[0])
