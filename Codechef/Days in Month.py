t=int(input())
for k in range(t):
    days=[4,4,4,4,4,4,4]
    day_count,dname=input().split()
    day_count=int(day_count)
    dname=str(dname)
    i=day_count-28
    day_list=['mon','tue','wed','thurs','fri','sat','sun']
    j=day_list.index(dname)
    while i>0:
        days[j]+=1
        j+=1
        if j>6:
            j=0
        i-=1
    print(days[0],days[1],days[2],days[3],days[4],days[5],days[6])
