def count_leap(n:int,case:bool)->int:
    lc=0
    if case:
        for i in range(2001,n):
            if i%100==0:
                if i%400==0:
                    lc+=1
            elif i%4==0:
                lc+=1
    else:
        for i in range(n,2001):
            if i%100==0:
                if i%400==0:
                    lc+=1
            elif i%4==0:
                lc+=1
    return lc
t=int(input())
day=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
for _ in range(t):
    year=int(input())
    leap=count_leap(year,year>=2001)
    if year>=2001:
        res=year-2001+leap
        print(day[res%7])
    else:
        res=2001-year+leap
        print(day[-res%7])
