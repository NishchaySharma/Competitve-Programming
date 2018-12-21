vowel={'a':0,'e':0,'i':0,'o':0,'u':0}
char=input()
for i in char:
    if i in vowel:
        vowel[i]+=1
for k,v in sorted(vowel.items()):
    if v!=0:
        print(k," in ",char," = ",v," time(s).")
