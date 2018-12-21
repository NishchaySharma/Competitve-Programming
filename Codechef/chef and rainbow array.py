t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if sum(set(l))==28 and l==l[::-1]:
        print('yes')
    else:
        print('no')
