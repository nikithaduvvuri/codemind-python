n=int(input())
Sum=0
mul=1
while n!=0:
    r=n%10
    Sum=Sum+r
    mul=mul*r
    n=n//10
if Sum==mul:
    print("Spy Number")
else:
    print("Not Spy Number")