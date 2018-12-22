a,b,c=1,2,997
for i in range(1,1000):
    flag=False
    for j in range(i+1,1000):
        k=1000-i-j
        if k<=j:
            break
        else:
            if i*i+j*j==k*k:
                res=i*j*k
                print(i,j,k,res)
                flag=True
                break
        if flag:
            break
        elif k<=i:
            break
print(res)
