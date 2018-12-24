s=input()
checkin=['a','A','e','E','i','I','o','O','u','U','Y','y']
res=''
for i in s:
    if i not in checkin:
        res+='.'
        res+=i.lower()
print(res)
