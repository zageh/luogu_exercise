import sys
input=sys.stdin.readline

n=int(input().strip())
a=list(map(int,input().strip().split()))

for i in range(n):
    if a[i]==0:
        a[i]=-1

pre=0
first={0:0}
ans=0

for i in range(1,n+1):
    if a[i-1]==1:
        pre+=1
    else:
        pre-=1

    if pre in first:
        ans=max(ans,i-first[pre])
    else:
        first[pre]=i

print(ans)