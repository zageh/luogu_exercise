import sys

data = sys.stdin.read().split()

h = int(data[0])
w = int(data[1])
q = int(data[2])
idx = 3

s = [['A'] * w for _ in range(h)]
op = [[('0', -1)]* w for _ in range(h)]

for i in range(q):
    r, c = [int(x) for x in data[idx: idx + 2]]
    r -= 1
    c -= 1
    x = data[idx + 2]
    idx += 3
    
    op[r][c] = (x, i)
    
for i in range(h - 1, -1, -1):
    new = '0'
    t = -1
    for j in range(w - 1, -1, -1):
        if op[i][j][0] == '0' and new =='0':
            continue
        
        if i > 0:
            if op[i-1][j][1] < op[i][j][1]:
                op[i-1][j] = op[i][j]
            
        if op[i][j][1] > t:
            new = op[i][j][0]
            t = op[i][j][1]
            
        s[i][j] = new
        
for i in range(h):
    sys.stdout.write(''.join(s[i]) + '\n')