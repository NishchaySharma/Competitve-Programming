t=int(input())
for test in range(t):
    m,n=map(int,input().split())
    rx,ry=map(int,input().split())
    n=int(input())
    l=input()
    x,y=l.count('R')-l.count('L'),l.count('U')-l.count('D')
    if x==rx and y==ry:
        print('Case ',test+1,': REACHED',sep='')
    elif x>m or y>n or x<0 or y<0:
        print('Case ',test+1,': DANGER',sep='')
    else:
        print('Case ',test+1,': SOMEWHERE',sep='')
