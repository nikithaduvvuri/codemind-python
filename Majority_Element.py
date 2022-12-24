n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    b.append(a.count(i))
for i in a:
    if a.count(i)==max(b):
        print(i)
        break