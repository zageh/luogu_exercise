import sys

data=sys.stdin.read().split()
n=int(data[0])
a=[int(x) for x in data[1:]]

ans=[0]*n

prefix=[a[0]]*n
backfix=[a[-1]]*n

for i in range(1,n):
    prefix[i]=max(a[i],prefix[i-1]+a[i])

for i in range(n-2,-1,-1):
    backfix[i]=max(a[i],backfix[i+1]+a[i])

for i in range(n):
    ans[i]=prefix[i]+backfix[i]-a[i]

print(*ans)