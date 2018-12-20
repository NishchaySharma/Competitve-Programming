t=int(input())
for i in range(t):
    s=input()
    s=list(s)
    count=0
    for i in range(0,len(s)-1):
        if s[i]!=s[i+1]:
            count+=1
    if count<=2:
        print('uniform')
    else:
        print('non-uniform')
