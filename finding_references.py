import sys
input=sys.stdin.readline
sys.setrecursionlimit(300000)
from collections import deque

n,m=map(int,input().split())
lst=[]
for _ in range(m):
    x,y=map(int,input().split())
    lst.append((x,y))

l=[[] for _ in range(n+1)]
for x,y in lst:
    l[x].append(y)
    
for i in range(1,n+1):
    if l[i]:
        l[i].sort()

vis=[False]*(n+1)
ans_dfs=[]
ans_bfs=[]

stack=[1]

while stack:
    cur=stack.pop()
    
    if vis[cur]:
        continue
    vis[cur]=True
    ans_dfs.append(cur)
    
    for next in reversed(l[cur]):
        if not vis[next]:
            stack.append(next)

print(*ans_dfs)

q=deque()
q.append(1)
ans_bfs.append(1)

vis=[False]*(n+1)
vis[1]=True
while q:
    cur=q.popleft()
    
    for x in l[cur]:
        if not vis[x]:
            q.append(x)
            ans_bfs.append(x)
            vis[x]=True
            
print(*ans_bfs)