import sys

data = sys.stdin.read().split()

n = int(data[0])
q = int(data[1])
m = int(data[2])

a = [0] + [int(x) for x in data[3: n + 3]]

ans = [0] * (n << 2)
plus = [0] * (n << 2)
mul = [1] * (n << 2)

def rs(p):
    return p << 1 | 1
def ls(p):
    return p << 1

def f(p, l, r, mv, pv):
    length = r - l + 1
    ans[p] = (ans[p] * mv + length * pv) % m
    mul[p] = (mul[p] * mv) % m
    plus[p] = (plus[p] * mv + pv) % m
        
def push_up(p):
    ans[p] = (ans[ls(p)] + ans[rs(p)]) % m
    
def build(p, l, r):
    plus[p] = 0
    mul[p] = 1
    
    if l == r:
        ans[p] = a[l] % m
        return 
    
    mid = (l + r) >> 1
    
    build(ls(p), l, mid)
    build(rs(p), mid + 1, r)
    
    push_up(p)
    
def push_down(p, l, r):
    mid = (l + r) >> 1

    f(ls(p), l, mid, mul[p], plus[p])
    f(rs(p), mid + 1, r, mul[p], plus[p])
    mul[p] = 1
    plus[p] = 0
        
def update(p, tl, tr, l, r, k, check):
    if tl <= l and tr >= r:
        if check == 1:
            f(p, l, r, k, 0)
        else:
            f(p, l, r, 1, k)
        return

    mid = (l + r) >> 1
    push_down(p, l, r)
    
    if mid >= tl:
        update(ls(p), tl, tr, l, mid, k, check)
    if mid < tr:
        update(rs(p), tl, tr, mid + 1, r, k, check)
        
    push_up(p)
    
def query(p, tl, tr, l, r):
    if tl <= l and tr >= r:
        return ans[p]
    
    res = 0
    
    mid = (l + r) >> 1
    push_down(p, l, r)
    
    if mid >= tl:
        res = (res + query(ls(p), tl, tr, l, mid)) % m
    if mid < tr:
        res = (res + query(rs(p), tl, tr, mid + 1, r)) % m
        
    return res % m

build(1, 1, n)

idx = n + 3

out = []
for _ in range(q):
    check = int(data[idx])
    
    if check == 3:
        x = int(data[idx + 1])
        y = int(data[idx + 2])
        
        idx += 3
        
        out.append(str(query(1, x, y, 1, n)))
        
    else:
        x = int(data[idx + 1])
        y = int(data[idx + 2])
        k = int(data[idx + 3])
        
        idx += 4
        
        update(1, x, y, 1, n, k, check)
        
sys.stdout.write('\n'.join(out))