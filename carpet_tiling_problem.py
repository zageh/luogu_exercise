import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

k=int(input().strip())
x,y=map(int,input().split())
ans=[]

def dfs(r,c,s,x,y):
    if s==1:
        return

    m=s//2

    if x<r+m and y<c+m:
        ans.append((r+m,c+m,1))
        dfs(r,c,m,x,y)
        dfs(r+m,c,m,r+m,c+m-1)
        dfs(r,c+m,m,r+m-1,c+m)
        dfs(r+m,c+m,m,r+m,c+m)

    elif x>=r+m and y<c+m:
        ans.append((r+m-1,c+m,3))
        dfs(r,c,m,r+m-1,c+m-1)
        dfs(r+m,c+m,m,r+m,c+m)
        dfs(r,c+m,m,r+m-1,c+m)
        dfs(r+m,c,m,x,y)

    elif x<r+m and y>=c+m:
        ans.append((r+m,c+m-1,2))
        dfs(r,c,m,r+m-1,c+m-1)
        dfs(r+m,c+m,m,r+m,c+m)
        dfs(r+m,c,m,r+m,c+m-1)
        dfs(r,c+m,m,x,y)

    else:
        ans.append((r+m-1,c+m-1,4))
        dfs(r,c,m,r+m-1,c+m-1)
        dfs(r+m,c+m,m,x,y)
        dfs(r,c+m,m,r+m-1,c+m)
        dfs(r+m,c,m,r+m,c+m-1)
        
dfs(1,1,1<<k,x,y)

for a,b,c in ans:
    print(a,b,c)