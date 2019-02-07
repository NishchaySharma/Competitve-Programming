def check(val1,val2):
    if sorted(val1)==sorted(val2):
        return 'YES'
    else:
        return 'NO'

t=int(input())
for i in  range(t):
    val=input()
    if len(val)%2==0:
        val1=val[:int(len(val)/2)]
        val2=val[int(len(val)/2):]
    else:
        val1=val[:int(len(val)/2)]
        val2=val[int(len(val)/2)+1:]
    print (check(val1,val2))
