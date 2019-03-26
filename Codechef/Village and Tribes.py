for _ in range(int(input())):
    s=input()
    d={'A':s.count('A'),'B':s.count('B')}
    vill,count='0',0
    for i in s:
        if i=='.' and vill!='0': count+=1
        elif vill!='0':
            if vill==i: d[vill]+=count
            else: vill=i
            count=0
        else: vill=i
    print(d['A'],d['B'])
