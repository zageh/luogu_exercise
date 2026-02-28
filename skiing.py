import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

mx=(1,-1,0,0)
my=(0,0,1,-1)

r,c=map(int,input().split())
h=[list(map(int,input().split())) for _ in range(r)]

dp=[[0]*c for _ in range(r)]
def dfs(i,j):
    if dp[i][j]!=0:
        return dp[i][j]

    best=1
    cur=h[i][j]
    for n in range(4):
        ni=i+mx[n]
        nj=j+my[n]
        if 0<=ni<r and 0<=nj<c and h[ni][nj]<cur:
            best=max(best,dfs(ni,nj)+1)

    dp[i][j]=best
    return best

ans=0
for i in range(r):
    for j in range(c):
        ans=max(ans,dfs(i,j))

print(ans)