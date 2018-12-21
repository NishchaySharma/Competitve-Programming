t=int(input())
for _ in range(t):
    s=input()
    d={'U':0,'D':0}
    i=0
    while True:
        j=i+1
        while True:
            if j>=len(s):
                break
            elif s[i]==s[j]:
                j+=1
            else:
                break
        if i==len(s):
            break
        else:
            d[s[i]]+=1
            i=j
    if d['U']<d['D']:
        print(d['U'])
    else:
        print(d['D'])
