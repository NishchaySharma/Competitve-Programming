for _ in range(int(input())):
    logo,flag=[],False
    for i in range(3):
        logo.append(list(input()))
    for i in range(2):
        for j in range(2):
            if logo[i][j]=='l' and logo[i+1][j]=='l' and logo[i+1][j+1]=='l':
                flag=True
                break
    if flag:
        print('yes')
    else:
        print('no')
