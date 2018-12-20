t=int(input())
for i in range(t):
    num=int(input())
    if num<9:
        print(num+1)
    elif num==9:
        print('11')
    else:
        l=len(str(num))
        case1=num
        case2=num
        if l%2==0:
            case1//=pow(10,l//2)
            case1=str(case1)
            case1=int(str(case1)+case1[::-1])
            case2//=pow(10,l//2)
            case2+=1
            case2=str(case2)
            case2=int(case2+case2[::-1])
        else:
            case1//=pow(10,l//2)
            case1=str(case1)
            case1=int(str(case1)+case1[l//2-1::-1])
            case2//=pow(10,l//2)
            case2+=1
            case2=str(case2)
            case2=int(case2+case2[l//2-1::-1])
        if case1>num:
            print(case1)
        else:
            print(case2) 
