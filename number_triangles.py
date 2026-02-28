import sys
input=sys.stdin.readline

r=int(input().strip())
dp=[[] for _ in range(r)]

for i in range(r):
    a=list(map(int,input().split()))
    for x in a:
        dp[i].append(x)

for i in range(1,r):
    for j in range(i+1):
        cand1 = 0 if j == 0 else dp[i-1][j-1]
        cand2 = 0 if j == i else dp[i-1][j]
        dp[i][j]+=max(cand1,cand2)

print(max(dp[r-1]))