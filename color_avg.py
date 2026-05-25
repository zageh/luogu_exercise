import sys

data = sys.stdin.read().strip().split()

r = 0
cr = 0
b = 0
cb = 0

n = int(data[0])
a = [int(x) for x in data[1: n + 1]]
c = data[-1]

for i in range(n):
    if c[i] == '0':
        r += a[i]
        cr += 1
    else:
        b += a[i]
        cb += 1
        

        
if (cr * b - cb * r) % n == 0:
    print(abs(cr * b - cb * r) // n)
else:
    print(-1)