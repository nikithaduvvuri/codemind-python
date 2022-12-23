def fun(n):
    res=0
    while n:
        d=n%10
        res=res*10+d
        n=n//10
    return res
def fun2(n):
    temp=n
    res=0
    while n:
        d=n%10
        res=res*10+d
        n=n//10
    if temp==res:
        return 1
    return 0
n=int(input())
while n:
    n=n+fun(n)
    if fun2(n):
        print(n)
        break