from collections import deque
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split(" ")))
    st=deque([])
    for i in range(n):
        if(st and a[st[-1]]>=a[i]):continue
        st.append(i)
    mn=mx=a[-1]
    cost=0
    for i in range(n-1,-1,-1):
        mn=min(a[i],mn)
        mx=max(a[i],mx)
        if i==st[-1]:
            st.pop()
        if(not st):
            cost+=(mx-mn)
            break
        if(a[st[-1]]<mn):
            cost+=(mx-mn)
            mx=float("-inf")
            mn=float("inf")
    print(cost)        