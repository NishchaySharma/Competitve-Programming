t=int(input())
for i in range(t):
    s=input()
    count=0
    l=['chef','chfe','cehf','cefh','cfeh','cfhe','hcef','hcfe','hfec','hfce','hecf','hefc',
       'echf','ecfh','efch','efhc','ehcf','ehfc','fech','fehc','fceh','fche','fhce','fhec']
    for j in l:
        count+=s.count(j)
    if count==0:
        print('normal')
    else:
        print('lovely',count)
