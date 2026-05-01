import sys
sys.setrecursionlimit(100000)

data=sys.stdin.read().split()

n=int(data[0])
k=int(data[1])

g=[[] for _ in range(n+1)]

idx=2
for _ in range(n-1):
    u=int(data[idx])
    v=int(data[idx+1])
    w=int(data[idx+2])
    g[u].append((v,w))
    g[v].append((u,w))
    idx+=3
    
cnt=[[0]*(k+1) for _ in range(n+1)]
danger=[[0]*(k+1) for _ in range(n+1)]

ans=0
def dfs(u,p):
    global ans 
    
    cnt[u][0]=1
    
    for v,w in g[u]:
        if v==p: continue
        dfs(v,u)
            
        for i in range(k):
            j=k-i-1
            
            c1=cnt[u][i]
            c2=cnt[v][j]
            
            if c1>0 and c2>0:
                s1=danger[u][i]
                s2=danger[v][j]+c1*w
                
                ans+=s1*c1+s2*c2
                
        for d in range(k):
            cnt[u][d+1]+=cnt[v][d]
            danger[u][d+1]+=danger[v][d]+w*cnt[v][d]
            
dfs(1,-1)

print(ans*2)