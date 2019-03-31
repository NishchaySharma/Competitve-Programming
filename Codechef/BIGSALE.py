t=int(input())
for i in range(t):
    n=int(input())
    loss=0.0
    for j in range(n):
        price,qty,sale=input().split(' ')
        price=int(price)
        qty=int(qty)
        sale=int(sale)
        newp=price*(sale+100)/100
        newp=newp*(100-sale)/100
        loss+=price-newp
        loss=float(loss*qty)
    print(loss)
