import sys
input = sys.stdin.readline

import heapq

out = []

test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    init = int(input(), 2)
    
    pq = [(0, init)]
    med = []
    dp = [float('inf')] * (1 << n)
    dp[init] = 0
    
    for row in range(m):
        t = int(input())
        cure = int(input().strip(), 2) ^ ((1 << n) - 1)
        harm = int(input().strip(), 2)
        
        heapq.heappush(med, (t, cure, harm))
    
    while pq:
        cur, mask = heapq.heappop(pq)
        
        if dp[mask] != cur:
            continue
        
        if mask == 0:
            break
                
        for t, cure, harm in med:
            new_mask = (mask & cure) | harm
            
            if dp[new_mask] > dp[mask] + t:
                dp[new_mask] = dp[mask] + t
                heapq.heappush(pq, (dp[new_mask], new_mask))      
            
    if dp[0] != float('inf'):
        out.append(str(dp[0]))
    else:
        out.append('-1')
        
sys.stdout.write('\n'.join(out))