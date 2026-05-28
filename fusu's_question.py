import sys

input = sys.stdin.buffer.readline

inf = -float('inf')

n, q = map(int, input().split())

tag = [0] * (n << 2)
ans = [0] * (n << 2)
rei = [inf] * (n << 2)

out = []

a = [0] + list(map(int, input().split()))
        
def push_up(p):
    ans[p] = ans[(p << 1)] if ans[(p << 1)] > ans[(p << 1 | 1)] else ans[(p << 1 | 1)]
        
def build(p, l, r):
    tag[p] = 0
    rei[p] = inf
    
    if l == r:
        ans[p] = a[l]
        return
    
    mid = (l + r) >> 1
    
    build((p << 1), l, mid)
    build((p << 1 | 1), mid + 1, r)
    
    push_up(p)
    
def push_down(p):
    lsp = p << 1
    rsp = (p << 1) | 1
    
    if rei[p] != inf:
        rei[lsp] = rei[p]
        tag[lsp] = 0
        ans[lsp] = rei[p]
        rei[rsp] = rei[p]
        tag[rsp] = 0
        ans[rsp] = rei[p]
        rei[p] = inf
        
    if tag[p]:
        ans[lsp] += tag[p]
        if rei[lsp] != inf:
            rei[lsp] += tag[p]
        else:
            tag[lsp] += tag[p]
        ans[rsp] += tag[p]
        if rei[rsp] != inf:
            rei[rsp] += tag[p]
        else:
            tag[rsp] += tag[p]
        tag[p] = 0    
    
def update(p ,tl, tr, l, r, k, check):
    if tl <= l and tr >= r:
        if check == 2:
            ans[p] += k
            if rei[p] != inf:
                rei[p] += k
            else:
                tag[p] += k
        else:
            rei[p] = k
            tag[p] = 0
            ans[p] = k
        return
    
    push_down(p)
    mid = (l + r) >> 1
    
    if tl <= mid:
        update(p << 1, tl, tr, l, mid, k, check)
    if tr > mid:
        update(p << 1 | 1, tl, tr, mid + 1, r, k, check)
        
    push_up(p)
    
def query(p, tl, tr, l, r):
    if tl <= l and tr >= r:
        return ans[p]
    
    res = inf
    
    mid = (l + r) >> 1
    push_down(p)
    
    if tl <= mid:
        res = query(p << 1, tl, tr, l, mid)
    if tr > mid:
        tmp = query(p << 1 | 1, tl, tr, mid + 1, r)
        res = res if res > tmp else tmp
        
    return res

build(1, 1, n)

for _ in range(q):
    data = list(map(int, input().split()))
    check = data[0]
    
    if  check == 3:
        l = data[1]
        r = data[2]

        out.append(str(query(1, l, r, 1, n)))
        
    else:
        l = data[1]
        r = data[2]
        x = data[3]

        update(1, l, r, 1, n, x, check)
        
sys.stdout.write('\n'.join(out))