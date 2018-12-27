for _ in range(int(input())):
    instruction=int(input())
    operations=list(map(int,input().split()))
    stack,flag=[],False
    for i in operations:
        if i==1:
            stack.append(1)
        else:
            if len(stack)==0:
                flag=True
                break
            else:
                stack.pop()
    if flag:
        print('Invalid')
    else:
        print('Valid')
