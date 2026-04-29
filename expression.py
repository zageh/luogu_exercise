import sys

data=sys.stdin.read().split()
n=int(data[0])
k=int(data[1])

a=[int(x) for x in data[2:]]

dp=[[[-1]*(k+1) for _ in range(n+1)]for row in range(n+1)]

for i in range(n):
    dp[i][i][0]=a[i]
    
for r in range(n):
    for l in range(r-1,-1,-1):
        for t in range(0,min(r-l,k)+1):
            for tl in range(0,min(r-l,k)-t+1):
                for d in range(l,r):
                    if dp[l][d][t]!=-1 and dp[d+1][r][tl]!=-1:
                        dp[l][r][t+tl]=max(dp[l][r][t+tl],dp[l][d][t]+dp[d+1][r][tl])
                    if t>0 and dp[l][d][t-1]!=-1 and dp[d+1][r][tl]!=-1:
                        dp[l][r][t+tl]=max(dp[l][r][t+tl],dp[l][d][t-1]*dp[d+1][r][tl])
                    if tl>0 and dp[l][d][t]!=-1 and dp[d+1][r][tl-1]!=-1:
                        dp[l][r][t+tl]=max(dp[l][r][t+tl],dp[l][d][t]*dp[d+1][r][tl-1])
                        
print(dp[0][n-1][k]) 