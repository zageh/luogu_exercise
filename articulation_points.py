import sys
sys.setrecursionlimit(1000000)

data=sys.stdin.read().split()

n=int(data[0])
m=int(data[1])
g=[[] for _ in range(n+1)]
low=[0]*(n+1)
dfn=[0]*(n+1)
vis=[False]*(n+1)

idx=2
while idx<len(data):
    a=int(data[idx])
    b=int(data[idx+1])
    g[a].append(b)
    g[b].append(a)
    idx+=2

timer=0
def tarjan(u,parent):
    global timer
    timer+=1
    dfn[u]=low[u]=timer
    c=0

    for v in g[u]:
        if not dfn[v]:
            c+=1
            tarjan(v,u)
            low[u]=min(low[u],low[v])
            if u!=parent and low[v]>=dfn[u]:
                vis[u]=True

        elif v!=parent:
            low[u]=min(low[u],dfn[v])

    if u==parent and c>=2:
        vis[u]=True

for i in range(1,n+1):
    if not dfn[i]:
        timer=0
        tarjan(i,i)

ans=[i for i in range(1,n+1) if vis[i]]
print(len(ans))
print(*ans)