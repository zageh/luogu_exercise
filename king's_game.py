import sys

data = sys.stdin.read().split()

n = int(data[0])
kl, kr = int(data[1]), int(data[2])

a = []
for i in range(n):
    l, r = int(data[i * 2 + 3]), int(data[i * 2 + 4])
    a.append((l, r, l * r))
    
a.sort(key = lambda x: x[2])

mx = 0
for l, r, _ in a:
    kr = kl // r
    kl *= l
    mx = max(kr, mx)
        
print(mx)