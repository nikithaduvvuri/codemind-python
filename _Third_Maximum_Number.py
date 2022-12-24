n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
if n==1:
    print(max(b))
elif n==2:
    print(max(b))
else:
    b.remove(max(b))
    b.remove(max(b))
    print(max(b))