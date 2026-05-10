import sys

data = sys.stdin.read().split()

inf = float('inf')

n = int(data[0])
m = int(data[1])
dp = [[inf]*(n+1) for _ in range(n+1)]
cnt = [[0]*(n+1) for _ in range(n+1)]

ans = [0.0] * (n+1)

idx = 2
for _ in range(m):
    s = int(data[idx])
    e = int(data[idx+1])
    v = int(data[idx+2])
    
    idx += 3
    
    cnt[s][e] = 1
    cnt[e][s] = 1
    
    dp[s][e] = min(v, dp[s][e])
    dp[e][s] = min(v, dp[e][s])
    
for k in range(1, n+1):
    for s in range(1, n+1):
        if s == k:
            continue
        
        for e in range(s+1, n+1):
            if e == k:
                continue
            
            if dp[s][k] + dp[k][e] < dp[s][e]:
                dp[s][e] = dp[s][k] + dp[k][e]
                cnt[s][e] = cnt[s][k] * cnt[k][e]
                
                dp[e][s] = dp[s][k] + dp[k][e]
                cnt[e][s] = cnt[s][k] * cnt[k][e]
                
            elif dp[s][k] + dp[k][e] == dp[s][e]: 
                cnt[s][e] += cnt[s][k] * cnt[k][e]
                cnt[e][s] += cnt[s][k] * cnt[k][e] 
                
for k in range(1, n+1):
    for s in range(1, n+1):
        if s == k:
             continue 
         
        for e in range(s+1, n+1):
            if e == k:
                continue
            
            if dp[s][k] + dp[k][e] == dp[s][e]:
                ans[k] += 2 * cnt[s][k] * cnt[k][e] / cnt[s][e]
                
for x in ans[1:]:
    print(f"{x:.3f}")