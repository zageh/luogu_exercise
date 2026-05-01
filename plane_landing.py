import sys
input=sys.stdin.readline

inf=10**7

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    p=[tuple(map(int,input().split())) for _ in range(n)]
    
    dp=[inf]*(1<<n)
    for mask in range(1<<n):
        if dp[mask]==inf:
            continue
        cur=dp[mask]
        
        for i in range(n):
            if mask>>i&1:
                continue
            
            t,d,l=p[i]
            start=max(cur,t)
            
            if start<=t+d:
                nxt=mask|(1<<i)
                dp[nxt]=min(dp[nxt],start+l)
                
print("YES" if dp[(1<<n)-1]!=inf else "NO")