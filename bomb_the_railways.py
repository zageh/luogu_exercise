import sys 
sys.setrecursionlimit(1000000)

data=sys.stdin.read().split()

n=int(data[0])
m=int(data[1])
dfn=[0]*(n+1)
low=[0]*(n+1)
timer=0
g=[[] for _ in range(n+1)]

idx=2
while idx<2*m+1:
    a=int(data[idx])
    b=int(data[idx+1])
    g[a].append(b)
    g[b].append(a)
    idx+=2
    
ans=[]

def tarjan(u,parent):
    global timer
    timer+=1
    dfn[u]=low[u]=timer
    
    for v in g[u]:
        if not dfn[v]:
            tarjan(v,u)
            low[u]=min(low[u],low[v])
            if low[v]>dfn[u]:
                ans.append((min(u,v),max(u,v)))
                
        elif v!=parent:
            low[u]=min(low[u],dfn[v])
            
for i in range(1,n+1):
    if not dfn[i]:
        tarjan(i,0)
        
ans.sort()
for a,b in ans:
    print(a,b)