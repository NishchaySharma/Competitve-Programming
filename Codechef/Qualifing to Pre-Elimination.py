for _ in range(int(input())):
    n,k=map(int,input().split())
    store=sorted(list(map(int,input().split())),reverse=True)
    till,count=store[k-1],0
    for i in store:
        if i >=till:
            count+=1
        else:
            break
    print(count)
