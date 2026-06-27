import sys
data = sys.stdin.read().split()

h = int(data[0])
w = int(data[1])
c = [x.strip() for x in data[2:]]

u, d, l, r = 0, h, 0, w
for i in range(h):
    ok = 1
    for j in range(w):
        if c[i][j] == '#':
            ok = 0
            break
        
    if ok:  
        u += 1
    else:
        break
    
for i in range(h-1, -1, -1):
    ok = 1
    for j in range(w):
        if c[i][j] == '#':
            ok = 0
            break
        
    if ok:  
        d -= 1
    else:
        break
    
for i in range(w):
    ok = 1
    for j in range(h):
        if c[j][i] == '#':
            ok = 0
            break
        
    if ok:  
        l += 1
    else:
        break
    
for j in range(w-1, -1, -1):
    ok = 1
    for i in range(h):
        if c[i][j] == '#':
            ok = 0
            break
    if ok:  
        r -= 1
    else:
        break
    
for i in range(u, d):
    print(c[i][l:r])