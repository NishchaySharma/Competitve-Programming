t=int(input())
for _ in range(t):
    s=list(input())
    for i in range(len(s)):
        if s[i]=='>':
            s[i]='<'
        elif s[i]=='<':
            s[i]='>'
    i=0
    cnt=0
    while i<len(s)-1:
        if s[i]=='>' and s[i+1]=='<':
            cnt+=1
            i+=1
        i+=1
    print(cnt)
