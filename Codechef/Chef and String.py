s=input()
c,ch,che,chef=0,0,0,0
for i in s:
    if i=='C':
        c+=1
    if i=='H'and c!=0:
        ch+=1
        c-=1
    if i=='E' and ch!=0:
        che+=1
        ch-=1
    if i=='F' and che!=0:
        chef+=1
        che-=1
print(chef)
