for _ in range(int(input())):
    n=int(input())
    if n>360: print('n n n')
    else:
        if 360/n == 360//n: ans1='y'
        else: ans1='n'
        ans2='y'
        if n<=26: ans3='y'
        else: ans3='n'
        print(ans1,ans2,ans3)
