for _ in range(int(input())):
    p,s=map(int,input().split())
    l,h=(p-pow(p**2-24*s,0.5))/12,(p+2*pow(p**2-24*s,0.5))/12
    print(round(l*l*h,2))
