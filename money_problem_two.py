import sys
input=sys.stdin.readline

n,w=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
mod=10**9+7

dp=[0]*(w+1)
dp[0]=1
for i in range(1,w+1):
    for x in a:
        if i<x:
            break
        dp[i]=(dp[i]+dp[i-x])%mod

print(dp[w])