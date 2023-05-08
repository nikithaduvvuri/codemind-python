s=input()
s=s.lower()
s=s.split(' ')
c=0
a=['a','e','i','o','u']
for i in s:
    x=list(i)
    if x[0] in a and x[-1] not in a:
        c+=1
print(c)        