import sys

data=sys.stdin.read().split()

n = int(data[0])
a = int(data[1])
b = int(data[2])

dp=[[[0]*(b+1) for _ in range(a+1)] for row in range(n+1)]

for i in range(a+1):
    for j in range(b+1):
        dp[1][i][j] = 1
        
if n == 1:
    print((a + 1) * (b + 1))
    sys.exit()
        
for layer in range(2,n+1):
    for i in range(a+1):
        for j in range(b+1):
            for li in range(i+1):
                for lj in range(j+1):
                    dp[layer][i][j] += dp[layer-1][li][lj]
                    
ans=0
for i in range(a+1):
    for j in range(b+1):
        ans += dp[n][i][j]
        
print(ans)