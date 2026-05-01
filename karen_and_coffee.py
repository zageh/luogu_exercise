import sys
input=sys.stdin.readline

n,k,q=map(int,input().split())

diff=[0]*200005
for _ in range(n):
    l,r=map(int,input().split())
    diff[l]+=1
    diff[r+1]-=1

cover=[0]*200005
for i in range(1,200005):
    cover[i]=cover[i-1]+diff[i]

total=[0]*200005
for i in range(1,200005):
    total[i]=total[i-1]+cover[i]

for _ in range(q):
    low,high=map(int,input().split())
    print(total[high]-total[low-1])