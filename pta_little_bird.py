import sys
from collections import deque

data = sys.stdin.buffer.read().split()

n = int(data[0])
d = [0] + [int(x) for x in data[1: n + 1]]
q = int(data[n + 1])
k = [int(x) for x in data[n + 2:]]

ans = []

for m in k:
    dp = [0] * (n + 1)
    dq = deque([1])
    
    for i in range(2, n + 1):
        while dq and dq[0] < i - m:
            dq.popleft()
           
        j = dq[0] 
        dp[i] = dp[dq[0]] + (d[j] <= d[i])
        
        while dq and (
            dp[dq[-1]] > dp[i] 
            or (dp[dq[-1]] == dp[i] and d[dq[-1]] <= d[i])):
            dq.pop()
            
        dq.append(i)
            
    ans.append(str(dp[n]))
    
sys.stdout.write('\n'.join(ans))