import sys

data = sys.stdin.read().split()

n = int(data[0])
k = int(data[1])

if k == 0:
    print(n)
    exit()
    
if n <= 1:
    print(0)
    exit()
    
a = [0] + [int(x) for x in data[2 :]]
a.sort()

l = len(a)
pref = [0] * l

for i in range(1, l):
    pref[i] = a[i] - a[i - 1]
    
div = k + a[0]
    
for i in range(1, l):
    if a[i] > div:
        div = i
        break
    
cnt = 2
        
for i in range(3, l):
    cnt += min(k + 1, pref[i])
    
print(cnt)