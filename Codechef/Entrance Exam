for _ in range(int(input())):
    n,k,e,m=map(int,input().split())
    scores=[]
    for _ in range(n-1):
        scores.append(sum(list(map(int,input().split()))))
    scores=sorted(scores,reverse=True)
    require=scores[k-1]-sum(list(map(int,input().split())))+1
    if require <= m: print(require if require>0 else 0)
    else: print('Impossible')
