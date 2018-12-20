t=int(input())
for test in range(t):
    n=int(input())
    count=0
    if n>0:
        team1=input()
        count+=1
        for i in range(n-1):
            tmp=input()
            if tmp==team1:
                count+=1
            else:
                count-=1
                team2=tmp
    if count==0:
        print('Draw')
    elif count>0:
        print(team1)
    else:
        print(team2)
