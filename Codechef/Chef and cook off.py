t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    if sum(l)==0:
        print('Beginner')
    elif sum(l)==1:
        print('Junior Developer')
    elif sum(l)==2:
        print('Middle Developer')
    elif sum(l)==3:
        print('Senior Developer')
    elif sum(l)==4:
        print('Hacker')
    else:
        print('Jeff Dean')
