import sys

data = sys.stdin.read().split()

n = int(data[0])
m = int(data[1])
judge = data[2:]

edge = [[False]* (n + 1) for _ in range(n + 1)]
indeg = [0] * (n + 1)

def check():
    deg = indeg[:]
    ans = ''
    unique = True
    
    for _ in range(n):
        zeros = []
        
        for i in range(n):
            if deg[i] == 0:
                if zeros:
                    unique = False
                zeros.append(i)
                
        if len(zeros) == 0:
            return -1,""
        
        u = zeros[0]
        ans += chr(u + ord('A'))
        
        deg[u] = -1
        
        for v in range(n):
            if edge[u][v]:
                deg[v] -= 1
                
    if unique:
        return 1, ans
    else:
        return 0, ""
    
    
for i in range(m):
    a = ord(judge[i][0]) - ord('A')
    b = ord(judge[i][2]) - ord('A')
    
    if not edge[a][b]:
        edge[a][b] = True
        indeg[b] += 1
    
    state, ans = check()
    
    if state == 1:
        print(f'Sorted sequence determined after {i + 1} relations: {ans}.')
        sys.exit()

    if state == -1:
        print(f'Inconsistency found after {i + 1} relations.')
        sys.exit()
        
print("Sorted sequence cannot be determined.")