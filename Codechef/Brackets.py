t=int(input())
for _ in range(t):
    s=input()
    stack=[]
    max_bal,bal=0,0
    for i in s:
        if i=='(':
            stack.append(i)
            bal+=1
            max_bal=max(bal,max_bal)
        else:
            stack.pop()
            bal-=1
    for _ in range(max_bal):
        print('(',end='')
    for _ in range(max_bal):
        print(')',end='')
    print()
