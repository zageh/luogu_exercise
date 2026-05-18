import sys

data = sys.stdin.read().split()

mod = 998244353

n = int(data[0])
a = [int(x) for x in data[1:]]

a.sort()
total = sum(a)
dp = [0] * (total + 1)
dp[0] = 1

ans = 0
pre = 0
for val in a:
    for j in range(total + 1):
        if not dp[j]:
            continue
        
        plus = j + val
        ex = max((plus + 1) // 2, val)
        ans = (ans + ex * dp[j]) % mod
        
    for j in range(total - val, -1, -1):
        if dp[j]:
            dp[j + val] = (dp[j + val] + dp[j]) % mod
                
print(ans)