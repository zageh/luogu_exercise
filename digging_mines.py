import sys
input=sys.stdin.readline

n=int(input())
num=list(map(int,input().split()))
c=[[]for _ in range(n+1)]
route=[[] for _ in range(n+1)]
end=[]
dp=[0]*(n+1)
for i in range(1,n):
    row=list(map(int,input().split()))
    for j in range(0,n-i):
        if row[j]==1:
            c[i].append(i+j+1)

for i in range(1,n+1):
    dp[i]=num[i-1]
    route[i]=[i]
    if len(c[i])==0:
        end.append(i)
        
for i in range(1,n+1):
    for x in c[i]:
        cand=dp[i]+num[x-1]
        if cand>dp[x]:
            dp[x]=cand
            route[x]=route[i]+[x]
        
ans=0
loc=0
for x in end:
    if dp[x]>ans:
        ans=dp[x]
        loc=x
print(' '.join(map(str,route[loc])))
print(ans)