import sys
import heapq

start = sys.stdin.read().strip()
t = '123804765'
target = [0] * 9

init_dist = 0
for i in range(1, 9):
    
    p = -1
    
    for j in range(9):
        if start[j] == str(i):
            p = j
        if t[j] == str(i):
            target[i] = j
            
    init_dist += (abs(target[i] //3 - p // 3)+ abs(target[i] % 3 - p % 3))
    
pq = [(init_dist, 0, init_dist, start)]
dist = {start:0}

while pq:
    f, p, h, s = heapq.heappop(pq)
    
    if p != dist[s]:
        continue
    
    if s == t:
        print(p)
        sys.exit()
    
    space = -1
    for i in range(9):
        if s[i] == '0':
            space = i
            break
        
    move = []
    
    if space // 3 != 0:
        move.append(space - 3)
        
    if space // 3 != 2:
        move.append(space + 3)
        
    if space % 3 != 0:
        move.append(space - 1)
        
    if space % 3 != 2:
        move.append(space + 1)
        
    for change in move:
        new_dist = (abs(space % 3 - target[int(s[change])] % 3) + abs(space // 3 - target[int(s[change])] // 3)) - (abs(change % 3 - target[int(s[change])] % 3) + abs(change // 3 - target[int(s[change])] // 3))
        
        new = [s[i] for i in range(9)]
        new[space], new[change] = new[change], new[space]
        
        if ''.join(new) not in dist or dist[''.join(new)] > p + 1:
            dist[''.join(new)] = p + 1
            heapq.heappush(pq,(f + new_dist + 1, p + 1, h + new_dist, ''.join(new)))
              
print(-1)