import sys

data=sys.stdin.read().split()

k=int(data[0])
a=data[1:]

dp=[0]*10

for i in range(k):
    s=int(a[i][0])
    e=int(a[i][-1])
    dp[e]=max(dp[e],dp[s]+1)

print(k-max(dp))