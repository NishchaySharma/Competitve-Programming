vowels=['a','e','i','o','u']
found={'a':0,'e':0,'i':0,'o':0,'u':0}
data=input('Enter a word = ')
for ch in data:
    if ch in vowels:
        found[ch]+=1
cntr=0
for k,v in sorted(found.items()):
    if v!=0:
        cntr+=1
        print(k,' is ',v,' time(s).')
if cntr==0:
    print('No vowel found !')
