import sys
sys.setrecursionlimit(1000000)

data = sys.stdin.read().split()

n = int(data[0])
k = int(data[1])
a = [int(x) for x in data[2:]]

maxb = (max(max(a), k)).bit_length() - 1

trie = [[0, 0], [0, 0]]
cnt = [0, 0]

def insert(x):
    p = 1
    cnt[p] += 1
    
    for i in range(maxb, -1, -1):
        b = (x >> i) & 1
        
        if not trie[p][b]:
            trie[p][b] = len(trie)
            trie.append([0, 0])
            cnt.append(0)
            
        p = trie[p][b]
        cnt[p] += 1
        
for x in a:
    insert(x)
    
def dfs(u, s):
    if u == 0:
        return 0
    
    if s == -1:
        return cnt[u]
    
    b = (k >> s) & 1
    
    l = trie[u][0]
    r = trie[u][1]
    
    if b == 0:
        return max(
            dfs(l, s - 1),
            dfs(r, s - 1)
        )
        
    else:
        return max(
            cnt[l] + dfs(r, s - 1),
            cnt[r] + dfs(l, s - 1)
        )
        
ans = dfs(1, maxb)

print(ans)