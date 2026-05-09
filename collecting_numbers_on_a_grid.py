import sys

data = sys.stdin.read().split()

n = int(data[0])
t = len(data) // 3

graph =[[0]*(n+1) for _ in range(n+1)]

idx = 1
for _ in range(t):
    x = int(data[idx])
    y = int(data[idx+1])
    v = int(data[idx+2])
    
    graph[x][y] = v
    idx +=3
    
dp = [[[0]*(n+1) for _ in range(n+1)] for row in range(2*n+1)]

for k in range(2,2*n+1):
    for x1 in range(1,n+1):
        for x2 in range(x1,n+1):
            
            y1 = k - x1
            y2 = k - x2
            
            if 0<y1<=n and 0<y2<=n:
                p = max(dp[k-1][x1-1][x2],
                        dp[k-1][x1][x2],
                        dp[k-1][x1][x2-1],
                        dp[k-1][x1-1][x2-1])   
                
                if x1 == x2:
                    dp[k][x1][x2] = graph[x1][y1] + p
                else:
                    dp[k][x1][x2] = graph[x1][y1] + graph[x2][y2] + p
                         
print(dp[2*n][n][n])