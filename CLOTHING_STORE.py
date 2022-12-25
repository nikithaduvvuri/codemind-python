n=int(input())
a=list(map(int,input().split()))
b=set(a)
sum=0
for i in b:
    sum+=a.count(i)//2
print(sum)    