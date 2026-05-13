import sys

data = sys.stdin.read().split()

n = int(data[0])
m = int(data[1])
a = [int(x) for x in data[2:]]
b = [0] * (n+1)

init = sum(a)

nin = [[0] * (n+1) for _ in range(m+1)]
nout = [[0] * (n+1) for _ in range(m+1)]

def flip(x):
    if x == 0:
        return 0
    
    s = bin(x)[2:]
    return int(s[::-1],2)

for i in range(n):
    b[i] = flip(a[i]) - a[i]  
    
nin[1][0] = b[0]

    
for i in range(1, n):
    for t in range(1, min(i, m)+1):
        nin[t][i] = max(nin[t][i-1], nout[t-1][i-1]) + b[i]
        nout[t][i] = max(nin[t][i-1], nout[t][i-1])
        
ans = -float('inf')
for t in range(m+1):
    ans = max(ans, nin[t][n-1], nout[t][n-1])
    
ans += init

print(ans)