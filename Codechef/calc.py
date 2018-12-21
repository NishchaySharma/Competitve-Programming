ch='Y'
while ch!='N':
    print("1 Add\n2 Sub\n3 Mull\n4 Div\n")
    req=int(input())
    print('Enter 2 numbers respectively : ')
    a,b=input().split()
    a=float(a)
    b=float(b)
    if ch==1:
        print('Sum = ',a+b)
    elif ch==2:
        print('Diff = ',a-b)
    elif ch==3:
        print('Mull = ',a*b)
    elif ch==4:
        print('Div = ',a/b)
