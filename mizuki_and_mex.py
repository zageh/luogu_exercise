import sys
input = sys.stdin.readline

def check(x):
    used = 0
    cost = 1
    
    for i in range(x - 1, 1, -1):
        have = a[i] if i <= n else 0
        
        if have < cost:
            used += have
            cost += cost - have
            
        else:
            used += cost
            
        if sa - used < 2 * cost:
            return False
        
    return sa - used >= 2 * cost

out = []
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sa = sum(a)
    
    if sa == 1:
        for i in range(n + 1):
            if a[i]:
                out.append(str(max(1, i)))
                break  
        continue
     
    l, r = 0, n + 66
    
    while l < r:
        mid = (l + r + 1) >> 1
        
        if check(mid):
            l = mid
            
        else:
            r = mid - 1
            
    out.append(str(r))
    
sys.stdout.write('\n'.join(out))