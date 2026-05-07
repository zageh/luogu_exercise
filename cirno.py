import sys
from collections import deque

data = sys.stdin.read().split()

n = int(data[0])
l = int(data[1])
r = int(data[2])
a = [int(x) for x in data[3:]]

dp = [-10**18] * (n + 1)
dp[0] = 0

dq = deque()

for i in range(l, n+1):
    j = i - l
    
    while dq and dp[dq[-1]] <= dp[j]:
        dq.pop()
    dq.append(j)

    while dq and dq[0] < i - r:
        dq.popleft()    
        
    dp[i] = dp[dq[0]] + a[i] 
        
ans = max(dp[n-r+1:])
print(ans)