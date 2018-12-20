t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    s=input()
    chef_count=0
    bro_count=0
    small=[97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
    cap=[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
    for j in s:
        if ord(j) in small:
            chef_count+=1
        if ord(j) in cap:
            bro_count+=1
    if chef_count<=k:
        if bro_count<=k:
            print('both')
        else:
            print('brother')
    elif bro_count<=k:
        print('chef')
    else:
        print('none')
