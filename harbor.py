import sys
from collections import deque, Counter

data = sys.stdin.read().split()

ans = []

n = int(data[0])

T = n
idx = 1
time = []
ship = []
while (T):
    t = int(data[idx])
    k = int(data[idx+1])
    x = [int(m) for m in data[idx+2:idx+k+2]]
    
    time.append(t)
    ship.append(x)
    
    idx += k+2
    T -= 1
    
dq = deque()

cnt = Counter()
var = 0

for i in range(n):
    t = time[i]
    
    while dq and time[dq[0]] <= t - 86400:
        for p in ship[dq[0]]:
            cnt[p] -= 1
            if cnt[p] == 0:
                var -= 1
        dq.popleft()
        
    dq.append(i)
    
    for s in ship[i]:
        if not cnt[s]:
            cnt[s] = 0
            var += 1
            
        cnt[s] += 1
            
    print(var)