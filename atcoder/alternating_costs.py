import sys
input = sys.stdin.readline

t = int(input())

out = []
for _ in range(t):
    a, b, x, y = map(int,input().split())
    
    x = abs(x)
    y = abs(y)
    if a > b:
        a, b = b, a
        x, y = y, x
    
    if x > y:
        cost = 2 * a * y
        dis = x - y
        
        d = b * (dis // 2 )+ a * ((dis + 1) // 2)
        r = 2 * a * dis
        if dis & 1:
            r -= a
        
        cost += min(r, d)
        
    else:    
        cost = 2 * a * x
        dis = y - x
        
        d = b * ((dis + 1) // 2) + a * (dis // 2)
        r = 2 * a * dis
        if dis & 1:
            r += a
            
        cost += min(r, d)
        
    out.append(str(cost))
    
sys.stdout.write('\n'.join(out))