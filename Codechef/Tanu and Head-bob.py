t=int(input())
for i in range(t):
    n=int(input())
    gstr=input()
    if 'I' in gstr:
        print('INDIAN')
    elif 'Y' in gstr:
        print('NOT INDIAN')
    else:
        print('NOT SURE')
