for _ in range(int(input())):
    l=[]
    for _ in range(10):
        l.append(list(map(int,input().split())))
    count=0
    for i in l:
        for j in i:
            if j<31:
                count+=1
    if count>=60:
        print('yes')
    else:
        print('no')
