import sys
input=sys.stdin.readline

n,w=map(int,input().split())
a=list(map(int,input().split()))

dp=[10**9]*(w+1)
dp[0]=0
for x in a:
    if x<=w:
        dp[x]=1
for i in range(1,w+1):
    for x in a:
        if i-x>=0:
            dp[i]=min(dp[i],dp[i-x]+1)

print(dp[w])