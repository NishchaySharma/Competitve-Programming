t=int(input())
for i in range(t):
    s1=input()
    s2=input()
    count1=0
    count2=0
    count3=0
    count4=0
    for i in range(len(s1)):
        if s1[i]=='?' and s2[i]!='?':
            count1+=1
        elif s1[i]!=s2[i] and s2[i]!='?':
            count3+=1
        if s2[i]=='?' and s1[i]!='?':
            count2+=1
        if s1[i]==s2[i] and s1[i]=='?':
            count4+=1
    print(count3,count4+count3+count2+count1)
