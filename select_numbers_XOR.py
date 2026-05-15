import sys
import math

data = sys.stdin.read().split()

n = int(data[0])
m = int(data[1])
x = int(data[2])
a = [0] + [int(x) for x in data[3: 3 + n]]

q = []
idx = 3 + n
for i in range(m):
    l = int(data[idx])
    r = int(data[idx+1])
    
    idx +=2
    q.append((l,r))
    
dp = [0] * (n+1)
p = {}

for i in range(1, n+1):
    cur = a[i]
    pair = cur ^ x
    
    pos = p.get(pair, 0)
    
    dp[i] = max(dp[i-1], pos)
    
    p[cur] = i
    
ans = []
for l, r in q:
    ans.append('yes' if l <= dp[r] else 'no')
        
sys.stdout.write('\n'.join(ans))