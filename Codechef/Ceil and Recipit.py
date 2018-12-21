t=int(input())
for i in range(t):
    p=int(input())
    menu=[2048,1024,512,256,128,64,32,16,8,4,2,1]
    count=0
    if p>4095:
        while p>=4096:
            count+=1
            p-=2048
    for i in menu:
        if i<=p:
            p-=i
            count+=1
    print(count)
