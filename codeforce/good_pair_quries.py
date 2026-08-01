import sys
input=sys.stdin.readline

t=int(input())
out = []
for _ in range(t):
    n, m = map(int, input().split())
    
    x = input().strip()
    y = input().strip()
    
    z = [0] * n
    o = [0] * n
    mi = [0] * n
    
    if x[0] == '0':
        if y[0] == '0':
            z[0] += 1
        else:
            mi[0] -= 1
    else:
        if y[0] == '0':
            mi[0] += 1
        else:
            o[0] += 1
     
    for i in range(1, n):
        o[i] = o[i - 1 ]
        z[i] = z[i - 1]
        mi[i] = mi[i - 1]
        if x[i] == '0':
            if y[i] == '0':
                z[i] += 1
            else:
                mi[i] -= 1
        else:
            if y[i] == '0':
                mi[i] +=  1
            else:
                o[i] += 1
                
    o = [0] + o
    z = [0] + z
    mi = [0] + mi
    
    while (m):
        m -= 1
        l, r = map(int, input().split())
        
        mix = abs(mi[r] - mi[l - 1])
        one = o[r] - o[l - 1]
        zero = z[r] - z[l - 1]
        
        if mix > one + zero:
            out.append("NO")
            
        else:
            out.append("YES")
            
sys.stdout.write('\n'.join(out))