import time
# 0 is for and in the number as 301 three hundered and one
single={1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}

double={1:3,11:6,12:6,13:8,14:8,15:7,16:7,
        17:9,18:8,19:8,2:6,3:6,4:5,5:5,6:5,
        7:7,8:6,9:6}

extra={0:3,1000:11,100:7}

count=0
def calculate(n:int)->int:
    if n in single:
        return single[n]
    elif n in double:
        return double[n]
    elif n==1000:
        return extra[1000]
    elif n==0:
        return 0
    elif n<100:
        return double[n//10]+calculate(n%10)
    else:
        if n%100!=0:
            return single[n//100]+extra[100]+extra[0]+calculate(n%100)
        else:
            return single[n//100]+extra[100]
res=0
for i in range(1,1001):
    res+=calculate(i)
print(res)
      
