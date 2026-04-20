import sys 
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n=int(input())
    ans=[0]*n
    a=list(map(int,input().split()))
    
    suf=[0]*(n+1)
    for i in range(n-1,-1,-1):
        suf[i]=suf[i+1]+a[i]
    ans[0]=suf[0]
    suf=suf[1:n]
    
    suf.sort(reverse=True)
    
    if n==1:
        print(ans[0])
        continue
    
    for i in range(1,n):
        ans[i]=ans[i-1]+suf[i-1]
            
    print(*ans)