t=int(input())
for i in range(t):
    val=int(input())
    tmp=1
    while tmp<val:
            tmp+=2
    if tmp==val:
        print('Odd')
    else:
        print('Even')
    
