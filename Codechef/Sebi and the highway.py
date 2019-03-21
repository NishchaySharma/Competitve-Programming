for _ in range(int(input())):
    s,sg,fg,d,t=map(int,input().split())
    d_diff=d*50
    s_=18*d_diff/(t*5) + s
    if abs(sg-s_)>abs(fg-s_): print('FATHER')
    elif abs(sg-s_)==abs(fg-s_): print('DRAW')
    else: print('SEBI')
