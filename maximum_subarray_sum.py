import sys
input=sys.stdin.readline

n=int(input().strip())
a=list(map(int,input().strip().split()))

pre=[0]*(n+1)
pre[0]=0

ans=-10**20
mini=0
for i in range(n):
    pre[i]=pre[i-1]+a[i]
    ans=max(ans,pre[i]-mini)
    mini=min(pre[i],mini)

print(ans)