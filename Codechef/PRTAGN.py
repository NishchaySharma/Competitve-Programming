def binary_one_count(n):
    if n>1: return n%2 + binary_one_count(n//2)
    return n

t = int(input())   
for _ in range(t):
    mylist = [0]*100001
    q = int(input())
    even, odd, s = 0, 0, set()
    for _ in range(q):
        x = int(input())
        if x not in s:
            for i in s.copy():
                s.add(i^x)
                if binary_one_count(i^x)%2 == 0: even+=1
                else: odd+=1
            s.add(x)
            if binary_one_count(x)%2 == 0: even+=1
            else: odd+=1
        print(even, odd)
