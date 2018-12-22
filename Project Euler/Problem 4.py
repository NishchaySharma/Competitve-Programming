res=1
for i in range(100,999):
    for j in range(i+1,1000):
        if str(i*j)==str(i*j)[::-1]:
            if res<i*j:
                res=i*j
                a,b=i,j
print(res,a,b)
