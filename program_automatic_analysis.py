import sys
input = sys.stdin.readline

ans = []
t = int(input())
for _ in range(t):
    mp = {}
    
    n = int(input())
    p = [0] * (2 * n + 1)
    relation = []
    ok = True
    
    for i in range(2 * n + 1):
        p[i] = i 
    
    def get_id(x):
        if x not in mp:
            mp[x] = len(mp)
            
        return mp[x]
    
    def find(x):
        while x != p[x]:
            p[x] = p[p[x]]
            x =p[x]
            
        return x
    
    def union(x, y):
        fx = find(x)
        fy = find(y)
        if fx != fy:
            p[fx] = fy
    
    for r in range(n):
        u, v, j = list(map(int,input().split()))
        u = get_id(u)
        v = get_id(v)
        if j == 1:
            union(u, v)
        else:
            relation.append((j, u, v))

    for j, u, v in relation:
        if j == 0:
            if find(u) == find(v):
                ok = False
                break
            
    ans.append('YES' if ok else 'NO')
    
sys.stdout.write('\n'.join(ans))