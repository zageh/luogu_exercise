import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input().strip())
    a=list(map(int,input().strip().split()))
    best=[0]*n
    mx=0
    pos=0
    
    for i in range(n):
        if a[i]>mx:
            mx=a[i]
            pos=i
        elif a[i]==mx:
            pos=i
        best[i]=pos
        
    cnt=0
    r=n-1
    while r>=0:
        cnt+=1
        r=best[r]-1
        
    print(cnt)