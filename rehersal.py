import sys

data = sys.stdin.read().split()

n = int(data[0])
a = [int(x) for x in data[1:]]
diff = [(a[i] - a[i - 1]) for i in range(1, n)]

if n == 1:
    print(0)
    sys.exit()

def cut(cur, pre):
    p = 1
    tot = 2
    while tot * pre < cur:
        p += 1
        tot += 2 ** p
        
    return p

def s(r, t):
    ret = 0
    for _ in range(t):
        ret += r
        r = (r + 1) // 2
    return ret

def last(cur, pre):
    t = cut(cur, pre)
    
    l, r = 1, cur
    
    while l < r:
        mid = (l + r + 1) >> 1
        
        if s(mid, t) <= cur:
            l = mid
        else:
            r = mid - 1
            
    return r

pre = diff[0]
cnt = 0
for cur in diff[1:]:
    if cur <= 2 * pre:
        pre = cur
        continue
    
    cnt += cut(cur, pre) - 1
    pre = last(cur, pre)
    
print(cnt)