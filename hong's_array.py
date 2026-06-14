import sys

data = sys.stdin.read().split()

n = int(data[0])
a = [int(x) for x in data[1 :]]

x = 0
for y in a:
    x ^= y
    
if x != 0:
    print(-1)
    exit()
    
ans = 0
for bit in range(30):
    cnt = 0
    cur = 0
    
    for x in a:
        cur ^= (x >> bit) & 1
        cnt += cur
        
    ans += min(cnt, n - cnt)
    
print(ans)