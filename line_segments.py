import sys
input=sys.stdin.readline

n=int(input().strip())
row=[]
dp=[[0,0] for _ in range(n)]
for _ in range(n):
    l,r=map(int,input().split())
    row.append((l,r))

dp[0][0],dp[0][1]=2*row[0][1]-1-row[0][0],row[0][1]-1

for i in range(1,n):
    cl,cr=row[i]
    l,r=row[i-1]

    dp[i][1]=min(dp[i-1][0]+abs(l-cl)+1+cr-cl,dp[i-1][1]+abs(r-cl)+1+cr-cl)

    dp[i][0]=min(dp[i-1][0]+abs(l-cr)+1+cr-cl,dp[i-1][1]+abs(r-cr)+1+cr-cl)

el,er=row[n-1]
print(min(dp[n-1][0]+n-el,dp[n-1][1]+n-er))