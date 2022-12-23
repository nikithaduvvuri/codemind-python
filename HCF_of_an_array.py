n=int(input())
a=list(map(int,input().split()))
for i in range(1,max(a)+1):
    x=0
    for j in range(0,len(a)):
        if a[j]%i==0:
            x+=1
    if x==len(a):
        res=i
print(res)        
        