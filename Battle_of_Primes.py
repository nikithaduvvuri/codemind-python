def prime(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
a=int(input())        
b=int(input())
k=a+b
r=1
while True:
    if prime(k+r):
        print(r)
        break
    r=r+1