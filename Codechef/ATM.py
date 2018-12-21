x,y=input().split()
x=int(x)
y=float(y)
if x%5==0:
    if x+.5<=y:
        y-=(x+.5)
print('%.2f'%y)
