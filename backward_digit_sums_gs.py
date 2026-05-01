import sys
sys.setrecursionlimit(1000000)

data=sys.stdin.read().split()
n=int(data[0])
s=int(data[1])

dp=[[0]*(n+1) for _ in range(n+1)]
dp[1][1]=1
for i in range(2,n+1):
    for j in range(1,i+1):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
      
vis=[False]*(n+1)
def dfs(path,added,i):
    global n,s
    if added>s:
        return
    
    if i==n:
        if added==s:
            print(*path)
            sys.exit()
        return
    
    for nxt in range(1,n+1):
        if not(vis[nxt]):
            vis[nxt]=True
            dfs(path+[nxt],nxt*dp[n][i+1]+added,i+1)
            vis[nxt]=False
            
dfs([],0,0)