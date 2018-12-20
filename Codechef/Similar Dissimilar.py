t=int(input())
for _ in range(t):
    l1=set(map(str,input().split()))
    l2=set(map(str,input().split()))
    if len(l1.intersection(l2))>=2:
        print('similar')
    else:
        print('dissimilar')
