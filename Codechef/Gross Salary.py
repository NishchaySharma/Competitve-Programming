t=int(input())
for i in range(t):
    b_sal=int(input())
    if b_sal<1500:
        hra=0.1*b_sal
        da=0.9*b_sal
    else:
        hra=500
        da=0.98*b_sal
    print(float(b_sal+hra+da))
