import sys
input=sys.stdin.readline

n, k=map(int, input().split())
lst=[0] * n
s= 0

for i in range(n):
    lst[i]=int(input())
    s+=lst[i]

init=s//k

if init==0:
    print(0)
    exit()

l=1
r=init
ans=0

while l<=r:
    mid=(l+r)//2

    cnt = 0
    for i in lst:
        cnt += i // mid
        if cnt>= k:
            break

    if cnt>=k:
        ans=mid
        l=mid+1
    else:
        r=mid-1

print(ans)