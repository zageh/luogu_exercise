import sys

data = sys.stdin.read().split()

idx = 2
n = int(data[0])
m = int(data[1])
birds = []
cnt = [0] * (n + 1)
tot = 0

for _ in range(n):
    a, d, b = [int(x) for x in data[idx : idx + 3]]
    idx += 3
    
    if cnt[a] == 0:
        tot += 1
    
    cnt[a] += 1
    if a != b:
        birds.append((d, a, b))
    
birds.sort()
n = len(birds)

idx = 0
for i in range(1, m + 1):
    while idx < n and birds[idx][0] <= i:
        a = birds[idx][1]
        b = birds[idx][2]
        
        idx += 1
        
        cnt[a] -= 1
        cnt[b] += 1
        
        if cnt[a] == 0:
            tot -= 1
        if cnt[b] == 1:
            tot += 1
            

            
    print(tot)