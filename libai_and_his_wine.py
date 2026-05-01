import sys

mod=10**9+7

data=sys.stdin.read().split()

n=int(data[0])
m=int(data[1])

dp=[[[0]*(m+3) for _ in range(m+1)]for d in range(n+1)]
dp[0][0][2]=1

for i in range(n+1):
    for j in range(m+1):
        for x in range(m+1):
            if x>m-j:
                break
            if i>=1:
                if dp[i-1][j][x//2]>0 and x%2==0:
                    dp[i][j][x]=(dp[i-1][j][x//2]+dp[i][j][x])%mod
            if j>=1:
                if dp[i][j-1][x+1]>0 and x<m:
                    dp[i][j][x]=(dp[i][j][x]+dp[i][j-1][x+1])%mod
                    
print(dp[n][m-1][1]%mod)