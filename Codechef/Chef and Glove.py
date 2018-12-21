t=int(input())
for test in range(t):
    n=int(input())
    hand=list(map(int,input().split()))
    glove=list(map(int,input().split()))
    cnt1,cnt2=0,0
    for i in range(n):
        if hand[i]<=glove[i]:
            cnt1+=1
    for i in range(n):
        if hand[i]<=glove[n-i-1]:
            cnt2+=1
    if cnt1==n:
        if cnt2==n:
            print('both')
        else:
            print('front')
    elif cnt2==n:
        print('back')
    else:
        print('none')
