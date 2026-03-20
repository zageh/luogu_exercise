#这个状态压缩太吊了
import math
import sys
input=sys.stdin.readline

n=int(input().strip())
p=[(0.0,0.0)]
for _ in range(n):
    p.append(tuple(map(float,input().split()))) # type: ignore

dis=[[0.0]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        dis[i][j]=math.sqrt((p[i][0]-p[j][0])**2+(p[i][1]-p[j][1])**2)

num_state=1<<(n+1)
dp=[[float('inf')]*(n+1) for _ in range(num_state)]

dp[1][0]=0

for mask in range(1,num_state):
    for i in range(n+1):
        
        if not (mask&(1<<i)):
            continue
            
        if dp[mask][i]==float('inf'):
            continue

        for j in range(1,n+1):
            if not (mask&(1<<j)):
                new_mask=mask|(1<<j)
                new_dis=dp[mask][i]+dis[i][j]
                dp[new_mask][j]=min(dp[new_mask][j],new_dis)

full_state=(1<<(n+1))-1
ans=min(dp[full_state][j] for j in range(n+1))
print(f"{ans:.2f}")