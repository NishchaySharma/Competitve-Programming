l=int(input())
b=int(input())
if l*b>2*(l+b):
    print('Area',l*b,sep='\n')
elif 2*(l+b)>l*b:
    print('Peri',2*(l+b),sep='\n')
else:
    print('Eq',l*b,sep='\n')
