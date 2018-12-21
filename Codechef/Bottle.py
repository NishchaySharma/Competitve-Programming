a,b,c=input().split(' ')
d,e,f=input().split(' ')
g,h,i=input().split(' ')
tot=0
lst1=[]
lst2=[]
lst3=[]
lst1.extend([int(a),int(b),int(c)])
lst2.extend([int(d),int(e),int(f)])
lst3.extend([int(g),int(h),int(i)])
lst1=sorted(lst1)
lst2=sorted(lst2)
lst3=sorted(lst3)
tot+=int(lst1[0])+int(lst2[0])+int(lst3[0])
print(tot)
