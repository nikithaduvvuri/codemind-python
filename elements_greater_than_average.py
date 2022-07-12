n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in range(n):
    s=s+a[i]
    ave=s//n
for i in range(n):
    if a[i]>=ave:
        c=c+1
print(c)