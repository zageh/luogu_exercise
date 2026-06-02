import sys

data = sys.stdin.read().split()

n = int(data[0])
a = [int(x) for x in data[1:]]

ma = max(a)

def check(x):
    cnt = [0] * (ma + 1)
    s = 0
    
    for i in range(x, n):
        cnt[a[i]] += 1
        
        if cnt[a[i]] == 2:
            s += 1
            
    if s == 0:
        return True
    
    for i in range(n - x):
        cnt[a[i + x]] -= 1
        if cnt[a[i + x]] == 1:
            s -= 1
            
        cnt[a[i]] += 1
        if cnt[a[i]] == 2:
            s += 1
            
        if s == 0:
            return True
        
    return False

l, r = 0, n - 1
while l < r:
    mid = (l + r) >> 1
    
    if check(mid):
        r = mid
        
    else:
        l = mid + 1
        
print(n - r)