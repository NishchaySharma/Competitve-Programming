for _ in range(int(input())):
    l=int(input())
    s=input()
    head,tail,flag=0,0,True
    for i in s:
        if i=='H':
            if head==0:
                head=1
            else:
                flag=False
                break
        elif i=='T':
            if tail==0 and head==1:
                head=0
            else:
                flag=False
                break
    if head or tail: flag=False
    if flag:
        print('Valid')
    else:
        print('Invalid')
