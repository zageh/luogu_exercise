import sys
input=sys.stdin.readline

t,m=map(int,input().split())
lst=[]
dp=[0]*(t+1)
for _ in range(m):
    c,v=map(int,input().split())
    for i in range(c,t+1):
        dp[i]=max(dp[i],dp[i-c]+v)

print(dp[t])