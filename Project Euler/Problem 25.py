'''
    Long method with execution time around 5 minutes
'''
a,b,pos=1,1,3
c=a+b
while len(str(c))!=1000:
    pos+=1
    a,b=b,c
    c=a+b
    print(c)
print(pos)
