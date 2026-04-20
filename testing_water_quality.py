import sys

data=sys.stdin.read().split()
mid=len(data[0])

river=[[] for _ in range(2)]
for x in data[0]:
    river[0].append(x)
for x in data[1]:
    river[1].append(x)

s=-1
e=-1
inf=float('inf')
dp=[inf]*3

for i in range(mid):
    if river[0][i]=='#' or river[1][i]=='#':
        s=i
        break
for i in range(mid-1,-1,-1):
    if river[0][i]=='#' or river[1][i]=='#':
        e=i
        break
if s==-1 or s>e:
    print(0)
    sys.exit()
    
if river[0][s]=='#' and river[1][s]=='#':
    dp[2]=0
elif river[0][s]=='#':
    dp[0]=0
    dp[2]=1
elif river[1][s]=='#':
    dp[1]=0
    dp[2]=1
    
for i in range(s+1,e+1):
    p0,p1,p2=dp[0],dp[1],dp[2]
    
    if river[0][i]=='#' and river[1][i]=='#':
        dp[0]=inf
        dp[1]=inf
        dp[2]=min(p0,p1,p2)
        
    elif river[0][i]=='#':
        dp[0]=min(p0,p2)
        dp[1]=inf
        dp[2]=min(p0,p1,p2)+1
        
    elif river[1][i]=='#':
        dp[0]=inf
        dp[1]=min(p1,p2)
        dp[2]=min(p0,p1,p2)+1
        
    else:
        dp[0]=min(p0,p2)+1
        dp[1]=min(p1,p2)+1
        dp[2]=min(p1,p2,p0)+2
        
print(min(dp[0],dp[1],dp[2]))