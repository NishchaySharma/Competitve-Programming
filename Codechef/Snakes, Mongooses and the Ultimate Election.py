for _ in range(int(input())):
    s=list(input())
    snake=s.count('s')
    mon=s.count('m')
    size=len(s)
    for i in range(size):
        if s[i]=='m':
            if i-1!=-1 and s[i-1]=='s':
                s[i-1]=' '
                snake-=1
            elif i+1!=size and s[i+1]=='s':
                snake-=1
                s[i+1]=' '
    if snake<mon: print('mongooses')
    elif snake==mon: print('tie')
    else: print('snakes')
