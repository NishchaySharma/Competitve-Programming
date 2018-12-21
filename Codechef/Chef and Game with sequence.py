t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if n==1:
        print('1')
    elif n==2:
        if l[0]%2 != l[1]%2:
            print('2')
        else:
            print('1')
    else:
        cnt_e,cnt_o=0,0
        for i in l:
            if i%2==0:
                cnt_e+=1
            else:
                cnt_o+=1
        if (cnt_o==1 and cnt_e==0) or cnt_o%2==0:
            print('1')
        else:
            print('2')
