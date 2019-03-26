for _ in range(int(input())):
    n,chance=input().split()
    heap=list(map(int,input().split()))
    if n=='1' and heap[0]%2==0 and chance=='Dee': print('Dee')
    else: print('Dum')
