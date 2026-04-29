import sys
input=sys.stdin.readline
from bisect import bisect_right

n,m=map(int,input().strip().split())
p=list(map(int,input().strip().split()))
mid=n//2

left=p[:mid]
right=p[mid:]

L=[]
R=[]

def dfs1(i,c):
    if c>m:
        return
    if i==len(left):
        L.append(c)
        return
    dfs1(i+1,c+left[i])
    dfs1(i+1,c)

def dfs2(i,c):
    if c>m:
        return
    if i==len(right):
        R.append(c)
        return
    dfs2(i+1,c+right[i])
    dfs2(i+1,c)

dfs1(0,0)
dfs2(0,0)

R.sort()

ans=0
for x in L:
    ans+=bisect_right(R,m-x)

print(ans)