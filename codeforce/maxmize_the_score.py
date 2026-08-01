import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [0] * (2 * n + 1)
    dp[0] = 1
    p = [-1] * (n + 1)
    
    for i in range(2 * n):
        x = a[i]
        
        if p[x] == -1:
            p[x] = i
            if i > 0:
                dp[i] = dp[i - 1] + 1
                
        else:
            d = p[x]
            
            cand = 0
            if d > 0:
                cand += dp[d - 1]
                
            cand += (i - d + 1) ** 2
            
            dp[i] = max(dp[i - 1] + 1, cand)
            
    print(dp[2 * n - 1])