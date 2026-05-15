import sys
import math

data = sys.stdin.read().split()

n = int(data[0])
m = int(data[1])
k = int(data[2])
b = [0] + [int(x) for x in data[3: n + 3]]

cnt = [0] * 100005
ans = [0] * m

b_size = math.isqrt(n)
idx = n + 3
q = []
for i in range(m):
    l = int(data[idx])
    r = int(data[idx+1])
    
    idx += 2
    
    q.append((l // b_size, r, i, l))
    
q.sort(key = lambda x:(x[0], x[1] if x[0] & 1 else -x[1]))

cur_l, cur_r = 1, 0
val = 0

for _, r, id, l in q:
    while cur_r < r:
        cur_r += 1
        cnt[b[cur_r]] += 1
        val += 2 * cnt[b[cur_r]] - 1
        
    while cur_l > l:
        cur_l -= 1
        cnt[b[cur_l]] += 1
        val += 2 * cnt[b[cur_l]] - 1
        
    while cur_r > r:
        cnt[b[cur_r]] -= 1
        val -= 2 * cnt[b[cur_r]] + 1
        cur_r -= 1
        
    while cur_l < l:
        cnt[b[cur_l]] -= 1
        val -= 2 * cnt[b[cur_l]] + 1
        cur_l += 1
        
    ans[id] = val
    
sys.stdout.write('\n'.join(map(str,ans)) + '\n')