t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    r_count=s.count('R')
    g_count=s.count('G')
    b_count=s.count('B')
    print(n-max(r_count,g_count,b_count))N
