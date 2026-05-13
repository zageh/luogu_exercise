import sys

data = sys.stdin.read().split()

n = int(data[0])
m = int(data[1])

idx = 2
inf = float('inf')

dp = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x = int(data[idx])
    y = int(data[idx+1])
    w = int(data[idx+2])
    
    idx += 3
    
    if w < dp[x][y]:
        dp[x][y] = w
        dp[y][x] = w
        
for k in range(1, n+1):
    for s in range(1, n+1):
        if k == s:
            continue
        
        for e in range(s, n+1):
            if s == e:
                dp[s][e] = 0
            if k == e:
                continue
            
            if dp[s][k] + dp[k][e] < dp[s][e]:
                dp[s][e] = dp[s][k] + dp[k][e]
                dp[e][s] = dp[s][k] + dp[k][e]
                
ans = 0
for s in range(1, n+1):
    for e in range(s+1, n+1):
        ans += dp[s][e]
                
sub = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        cand = 0    
    
        for s in range(1, n+1):
            for e in range(s+1, n+1):
                match = min(dp[s][i] + dp[e][j],
                            dp[s][j] + dp[e][i])
                
                if match < dp[s][e]:
                    cand += dp[s][e] - match
                    
        if cand > sub:
            sub = cand
            
ans -= sub

print(ans)