s=input()
s=s.lower()
s=list(s)
a=[]
for i in s:
    if s.count(i)==1:
        a.append(i)
a.sort()
st='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'
for i in a:
    if i==' ':
        continue
    st+=i
print(st)    