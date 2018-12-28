for _ in range(int(input())):
    s,e,l,r=input().split()
    l,r=int(l),int(r)
    week=['saturday','sunday','monday', 'tuesday', 'wednesday', 'thursday','friday']
    startindex=week.index(s)
    endindex=week.index(e)
    if startindex<=endindex:
        size=endindex-startindex+1
    else:
        size=8-startindex+endindex
    count,res=0,-1
    for i in range(0,r+1,7):
        if size+i>=l and size+i<=r:
            count+=1
            if count==1:
                res=size+i
        if count==2:
            break
    if res==-1:
        print('impossible')
    elif count==1:
        print(res)
    else:
        print('many')
