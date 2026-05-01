import sys

data=sys.stdin.read().split()

n=int(data[0])
balance=400000

dp=[-10**9]*(2*balance+5)
dp[balance]=0

idx=1
l,r=balance,balance
for _ in range(n):
    s=int(data[idx])
    f=int(data[idx+1])
    idx+=2
    
    if s+f<0:
        continue
    
    if s>0:
        for i in range(r,l-1,-1):
            if dp[i]==-10**9:
                continue
            
            dp[i+s]=max(dp[i]+f,dp[i+s])
            
    if s<=0:
        for i in range(l,r+1):
            if dp[i]==-10**9:
                continue
            
            dp[i+s]=max(dp[i]+f,dp[i+s])
    
    r=max(r,r+s)
    l=max(min(l,l+s),200000)
        
ans=0
for i in range(balance,r+1):
    if dp[i]>=0:
        ans=max(ans,dp[i]+i-balance)
    
print(ans)