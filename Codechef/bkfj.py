entrada = int(input())
ff = 1
while entrada:
    entrada-=1
    f = input()
    f = f.split(" ")
    n = int(f[0])
    k = int(f[1])
    if k > n:
        nuevo_n = 0
    else:
        nuevo_n = n +1 - k
    print("Case " + str(ff)+": " +str(nuevo_n*(nuevo_n+1)//2))
    ff+=1
