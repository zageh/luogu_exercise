import sys

data= sys.stdin.read().strip().split()

n = int(data[0])
m = int(data[1])

c0 = [[] for _ in range(10 ** 5 + 1)]
c1 = [[] for _ in range(10 ** 5 + 1)]
c2 = [[] for _ in range(10 ** 5 + 1)]

idx = 2
for _ in range(m):
    u = int(data[idx])
    v = int(data[idx + 1])
    w = int(data[idx + 2])
    
    idx += 3
    
    du = 0
    dv = 0
    
    if w == 0:
        c0[u].append(v)
        c0[v].append(u)
    elif w == 1:
        c1[u].append(v)
        c1[v].append(u)
    else:
        c2[u].append(v)
        c2[v].append(u)
        
for i in range(1, n + 1):
    if c1[i]:
        if c2[i]:
            print(i,c1[i][0])
            print(i,c2[i][0])
            sys.exit()
            
        if c0[i]:
            print(i,c1[i][0])
            print(i,c0[i][0])
            sys.exit()
            
    if c0[i] and c1[i]:
        print(i,c0[i][0])
        print(i,c1[i][0])
        sys.exit()    
    
print(-1)